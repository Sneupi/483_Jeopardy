import spacy
import os
import re
import sqlite3


TITLE_PATTERN = re.compile(r'^\[\[([^:]*)\]\]$')
CATEGORY_PATTERN = re.compile(r'^categories:\s+(.*)$', re.IGNORECASE)
HEADER_PATTERN = re.compile(r'^\s*={2,5}(.*?)={2,5}\s*$')


try:
    SPACY_NLP = spacy.load("en_core_web_sm")
except:
    print('Not found "en_core_web_sm". Run in terminal "python3 -m spacy download en_core_web_sm".')
    exit(-1)


def index_passages(db_name, passages):
    '''Takes list of passage info (id, title, path) and indexes to SQL DB'''
    
    # Create tables
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS passage (
                            pid INT PRIMARY KEY, 
                            title TEXT,
                            path TEXT 
                        )''')
        
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_passage ON passage(pid)')
    
    # Index passages
    print(f"Indexing passages to {db_name}...")
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.executemany("INSERT INTO passage (pid, title, path) VALUES (?, ?, ?)", passages)
    print("Done.")


def fetch_row(db_name, pid):
    '''Fetches (title, path) by passage id 
    (i.e. Dense Passage Retrieval docID)'''
    
    with sqlite3.connect(db_name) as conn: 
        cursor = conn.cursor()
        cursor.execute("SELECT title, path FROM passage WHERE pid = ?", (pid,))
        result = cursor.fetchone()
        
        if result:
            return (result[0], result[1])
        return None


def refine_query(query: str):
    '''
    Tokenizes query, returning 
    only descriptive content words 
    most-relevant for Jeopardy clues.
    Retains phrases in double quotes as single entities.
    '''
    # Extract quoted phrases
    QUOTE = r'(\"[^\"]*\")'
    tokens = [t for t in re.split(QUOTE, query) if t]
    
    final_output = []

    for segment in tokens:
        # If the segment is already a quote, keep it as is
        if re.match(QUOTE, segment):
            final_output.append(segment)
            continue
        
        # 2. Process non-quoted segments with spaCy
        doc = SPACY_NLP(segment)
        i = 0
        while i < len(doc):
            token = doc[i]
            
            # Check if token is part of a Named Entity
            if token.ent_iob_ != 'O':
                
                # Get the full span of the entity
                ent = token.ent_type_
                start = i
                while i < len(doc) and doc[i].ent_type_ == ent:
                    i += 1
                entity_text = doc[start:i].text
                
                final_output.append(entity_text)
                    
            # If not an entity, apply Part-Of-Speech and Stopword filters
            else:
                if token.pos_ in {"NOUN", "PROPN", "ADJ"} and not token.is_stop:
                    final_output.append(token.text)
                i += 1

    # 3. Combine back into a single string
    result = " ".join(final_output)
            
    return result
    
    


def clean_body(body):
    '''Simple cleaning of MediaWiki syntax'''
    tpl_element = r'\[tpl\].*?\[\/tpl\]'
    links = r'\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|]'
    header_md = r'={2,5}'
    table_md = r'^\s*\|[^\n]*$'
    
    body = re.sub(r'(' + tpl_element + r'|' + links + r'|' + header_md + r'|' + table_md + r')', '', body, flags=re.DOTALL|re.IGNORECASE|re.MULTILINE)
    return body


def _yield_passages(path):
    '''
    Yields passages of wiki entries,
    contained in text file
    '''
    
    title = None
    passage = []
    header = ''
    
    is_empty = lambda p: all(s.isspace() for s in p)
    is_redirect = lambda p: '#redirect' in ''.join(p).lower()
    cleaned = lambda p: clean_body(''.join(p))
    
    with open(path) as file:
        for line in file:
            
            # collect to entries, yielding
            match_title = TITLE_PATTERN.match(line)
            match_header = HEADER_PATTERN.match(line)
            
            if match_title:
                if not is_empty(passage) and not is_redirect(passage):
                    yield title, cleaned([header] + passage)
                title = match_title.group(1)
                header = ''
                passage = []
                
            elif match_header:
                if not is_empty(passage) and not is_redirect(passage):
                    yield title, cleaned([header] + passage)
                header = match_header.group(1)
                passage = []
                
            else:
                passage.append(line)
            
    # EOF, yield last entry
    if not is_empty(passage) and not is_redirect(passage):
        yield title, cleaned([header] + passage)


def yield_passages(corpus):
    '''
    Yields passages of wiki entries,
    contained in text files, 
    contained in corpus directory
    '''
    # Chunking for Dense Passage Retrieval
    def chunk_text(text: str, chunk_size=100):
        words = text.split()
        for i in range(0, len(words), chunk_size):
            yield " ".join(words[i:i + chunk_size])
    
    # iterate files in dir
    for f in sorted(os.listdir(corpus)):                
        path = os.path.join(corpus, f)
        
        # skip all subdirs
        if os.path.isdir(path): continue
        print('Reading: ', path, end='\r')
        
        # iterate lines in file
        for title, passage in _yield_passages(path):
            
            # return in manageable chunks
            for chunk in chunk_text(passage):
                yield path, title, chunk
            
    print()


def get_questions(path):
    '''Get list of (category, clue, answer)'''
    
    questions = []
    
    with open(path) as q_file:
        
        cqa_list = [
            cqa.strip() 
            for cqa in q_file.read().split('\n\n') 
            if cqa.strip()
        ]
        
        for cqa in cqa_list:
            category, question, answer = cqa.split('\n')
            answer = answer.split('|') # delimit by '|'
            questions.append((category, question, answer))
        
    return questions
      

if __name__ == "__main__":
    
    # print questions
    for c,q,a in get_questions('assets/questions.txt'):
        print('Category:',c)
        print('Clue:',q)
        print('Clue (Refined):',refine_query(q))
        print('Answer:',a)
        print()
    
    passages = []
    
    # # print corpus
    # for i, (path, title, passage) in enumerate(yield_passages('assets/corpus-example')):
    #     print('Path:',path)
    #     print('Title:',title)
    #     print('Passage ID:',i)
    #     print('Passage:',passage)
    #     print('-'*80)
    #     passages.append((i,title,path)) # for later DB indexing
    
    # # index & test retrieve
    # EXAMPLE_DB = '.example.db'
    # index_passages(EXAMPLE_DB, passages)
    # print('330 -> ',fetch_row(EXAMPLE_DB, 330))
    # print('331 -> ',fetch_row(EXAMPLE_DB, 331))
    # print('333 -> ',fetch_row(EXAMPLE_DB, 333))
    # print('334 -> ',fetch_row(EXAMPLE_DB, 334))
    # os.remove(EXAMPLE_DB)