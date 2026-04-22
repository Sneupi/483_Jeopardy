import spacy
import os
import re

TITLE_PATTERN = re.compile(r'^\[\[([^:]*)\]\]$')
CATEGORY_PATTERN = re.compile(r'^categories:\s+(.*)$', re.IGNORECASE)
HEADER_PATTERN = re.compile(r'^\s*={2,5}(.*?)={2,5}\s*$')

try:
    SPACY_NLP = spacy.load("en_core_web_sm")
except:
    print('Not found "en_core_web_sm". Run in terminal "python3 -m spacy download en_core_web_sm".')
    exit(-1)


def refine_query(query: str):
    '''
    Tokenizes query, returning 
    only descriptive content words 
    most-relevant for Jeopardy clues
    '''
    doc = SPACY_NLP(query)
    
    # Extract Named Entities
    entities = [ent.text for ent in doc.ents]
    
    # Filter tokens by Part-of-Speech
    pos_filtered = [
        token.text for token in doc 
        if token.pos_ in {"NOUN", "PROPN", "ADJ"} and not token.is_stop
    ]
    
    # Combine and Deduplicate
    refined_tokens = set(pos_filtered).union(entities)
    
    return refined_tokens


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
    
    # iterate files in dir
    for f in sorted(os.listdir(corpus)):                
        path = os.path.join(corpus, f)
        
        # skip all subdirs
        if os.path.isdir(path): continue
        print('Reading: ', path, end='\r')
        
        # iterate lines in file
        for title, passage in _yield_passages(path):
            yield path, title, passage
            
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
    
    # print corpus
    for i, (path, title, passage) in enumerate(yield_passages('assets/corpus-example')):
        print('Path:',path)
        print('Title:',title)
        print('Passage ID:',i)
        print('Passage:',passage)
        print('-'*80)
    
    pass