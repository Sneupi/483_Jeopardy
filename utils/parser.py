
import os
import re

def clean_body(body):
    '''Simple cleaning of MediaWiki syntax'''
    body = re.sub(r'(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|]|\[tpl\].*?\[/tpl\])', '', body, flags=re.DOTALL|re.IGNORECASE)
    return body
    
def yield_docs(corpus_dir):
    '''
    Yields wiki entries contained in text 
    files contained in corpus directory
    '''
    
    title_pattern = re.compile(r"^\[\[([^\n:]*)\]\]$")
    title = None
    body = []
    
    # iterate files in dir
    for f in os.listdir(corpus_dir):                
        path = os.path.join(corpus_dir, f)
        
        # skip all subdirs
        if os.path.isdir(path): continue
        print('Reading: ', path, end='\r')
        
        # iterate lines in file
        with open(path) as file:
            for line in file:
                
                # collect to entries, yielding
                match = title_pattern.match(line)
                if match:
                    
                    # exclude redirects from yielded entries
                    body = clean_body(''.join(body))
                    if title and '#redirect' not in body.lower():
                        yield path, title, body
                    
                    # start new entry
                    title = match.group(1)
                    body = []
                else:
                    body.append(line)
                    
    # EOF, yield last entry
    body = clean_body(''.join(body))
    if title and '#redirect' not in body.lower():
        yield path, title, body
    