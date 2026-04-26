import spacy
import os
import re
import pickle

TITLE_PATTERN = re.compile(r'^\[\[([^:]*)\]\]$')
CATEGORY_PATTERN = re.compile(r'^categories:\s+(.*)$', re.IGNORECASE)
HEADER_PATTERN = re.compile(r'^\s*={2,5}(.*?)={2,5}\s*$')


try:
    SPACY_NLP = spacy.load("en_core_web_sm")
except:
    print('Not found "en_core_web_sm". Run in terminal "python3 -m spacy download en_core_web_sm".')
    exit(-1)


def save_pickle(obj, path):
    if os.path.exists(path): os.remove(path)
    with open(path, 'wb') as f: 
        pickle.dump(obj, f)
        
        
def load_pickle(path):
    with open(path, 'rb') as f:
        obj = pickle.load(f) 
    return obj


def refine_clue(clue: str):
    '''
    Returns distilled string, containing
    most-significant tokens to Jeopardy clues
    '''
    # Extract quoted phrases
    QUOTE = r'(\"[^\"]*\")'
    tokens = [t for t in re.split(QUOTE, clue) if t]
    
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
    
    

def clean_mediawiki(content):
    '''Simple cleaning of MediaWiki syntax'''
    tpl_element = r'\[tpl\].*?\[\/tpl\]'
    links = r'\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|]'
    header_md = r'={2,5}'
    table_md = r'^\s*\|[^\n]*$'
    
    content = re.sub(r'(' + tpl_element + r'|' + links + r'|' + header_md + r'|' + table_md + r')', '', content, flags=re.DOTALL|re.IGNORECASE|re.MULTILINE)
    return content

        
            
def yield_wiki_path(path):
    '''Yields wiki entries (title, content) contained in file'''
    
    title = None
    content = []
    
    with open(path) as file:
        for line in file:
            
            match_title = TITLE_PATTERN.match(line)
            
            if match_title:
                
                content = ''.join(content)
                if title:
                    yield title, content
                    
                title = match_title.group(1)
                content = []
                
            else:
                content.append(line)
            
    # EOF, yield last entry
    content = ''.join(content)
    if title:
        yield title, content



def yield_wiki_corpus(corpus):
    '''
    Yields wiki entries 
    (title, content)
    contained in text files, 
    contained in corpus directory.
    '''
    for f in sorted(os.listdir(corpus)):   
                     
        path = os.path.join(corpus, f)
        if os.path.isdir(path): continue
        print('Reading: ', path, end='\r')
        
        for title, content in yield_wiki_path(path):
            yield title, content
                     
    print()



def yield_questions(path):
    '''Yield sequence of category, clue, answer'''    
    
    with open(path) as file:
        
        cqa_list = [
            cqa.strip() 
            for cqa in file.read().split('\n\n') 
            if cqa.strip()
        ]
        
        for cqa in cqa_list:
            category, clue, answer = cqa.split('\n')
            answer = answer.split('|') # delimit by '|'
            yield category, clue, answer
      


def chunk_text(title, content, window_size=100, overlap=20):
    """Splits text into overlapping chunks prefixed with the title."""
    words = content.split()
    if not words:
        return []
    
    chunks = []
    for i in range(0, len(words), window_size - overlap):
        chunk = words[i : i + window_size]
        # Adding the title to each chunk improves DPR retrieval significantly
        full_text = f"{title}: {' '.join(chunk)}"
        chunks.append(full_text)
        if i + window_size >= len(words):
            break
    return chunks



if __name__ == "__main__":
    
    # print questions
    for category, clue, answers in yield_questions('assets/questions.txt'):
        print('Category:', category)
        print('Clue:', clue)
        print('Clue (Refined):', refine_clue(clue))
        print('Answer:', answers)
        print()
    
    wiki_titles = []
    wiki_redirects = {} # Don't save redirects; instead alias to existing pages
    wiki_content = []
    
    # print corpus
    i = 0
    for title, content in yield_wiki_corpus('assets/corpus-example'):
        
        # clean content
        content = clean_mediawiki(content)
        
        # if alias, track but dont actually index
        found = re.search(r'^\s*#redirect\s+(.*?)$', content, re.IGNORECASE|re.MULTILINE)
        if found:
            alias = found.group(1)
            if not wiki_redirects.get(title):
                wiki_redirects[title] = []
            wiki_redirects[title].append(alias)
            continue
        
        # subdivide into chunks
        for chunk in chunk_text(title, content):
            wiki_titles.append(title)
            wiki_content.append(chunk)
            
            line = '-'*50
            print(f'{i} --- (Chunked & Cleaned) {line}\n{chunk}\n')
            i += 1
    
    # print aliases
    print("List of Aliases:")
    for k, v in wiki_redirects.items():
        print('\t',k,'->',v)
    
    # index & test retrieve
    import pickle
    
    EXAMPLE_PKL = '.example.pkl'
    
    if os.path.exists(EXAMPLE_PKL): 
        os.remove(EXAMPLE_PKL)
        
    with open(EXAMPLE_PKL, 'wb') as f: 
        pickle.dump(wiki_titles, f)
    
    with open(EXAMPLE_PKL, 'rb') as f:
        temp = pickle.load(f)
        print('LOAD TOP ->',temp[0])
        print('LOAD END ->',temp[len(temp)-1])
    
    os.remove(EXAMPLE_PKL)
    
    print('".wiki" size (pages, include redirects):',len([_ for _ in yield_wiki_corpus('.wiki')]))
    