# Parses, cleans, and yields wiki entries from textfiles, or entire corpus

import os
import re

TITLE_PATTERN = re.compile(r'^\[\[([^:]*)\]\]$')
CATEGORY_PATTERN = re.compile(r'^categories:\s+(.*)$', re.IGNORECASE)
HEADER_PATTERN = re.compile(r'^\s*={2,5}.*?={2,5}\s*$')


def clean_body(body):
    '''Simple cleaning of MediaWiki syntax'''
    tpl_element = r'\[tpl\].*?\[\/tpl\]'
    links = r'\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|]'
    header_md = r'={2,5}'
    table_md = r'^\s*\|[^\n]*$'
    
    body = re.sub(r'(' + tpl_element + r'|' + links + r'|' + header_md + r'|' + table_md + r')', '', body, flags=re.DOTALL|re.IGNORECASE)
    return body


def yield_docs_path(path):
    '''
    Yields docs from wiki
    formatted text file:
    (title, categories, intro, body)
    '''
    
    title = None
    categories = []
    intro = []
    body = []
    
    with open(path) as file:
        for line in file:
            
            # collect to entries, yielding
            match_title = TITLE_PATTERN.match(line)
            match_categories = CATEGORY_PATTERN.match(line)
            match_header = HEADER_PATTERN.match(line)
            
            if match_title:
                
                # exclude redirects from yielded entries
                intro = clean_body(''.join(intro))
                body = clean_body(''.join(body))
                if title and '#redirect' not in intro.lower():
                    yield title, categories, intro, body
                
                # start new entry
                title = match_title.group(1)
                categories = []
                intro = []
                body = []
                
            elif match_categories:
                categories = match_categories.group(1).split(',')
                
            elif not body and not match_header:
                intro.append(line)
                
            else:
                body.append(line)
            
    # EOF, yield last entry
    intro = clean_body(''.join(intro))
    body = clean_body(''.join(body))
    if title and '#redirect' not in intro.lower():
        yield title, categories, intro, body


def yield_docs_corpus(corpus):
    '''
    Yields wiki entries contained in text 
    files contained in corpus directory:
    (path, title, categories, intro, body)
    '''
    
    # iterate files in dir
    for f in os.listdir(corpus):                
        path = os.path.join(corpus, f)
        
        # skip all subdirs
        if os.path.isdir(path): continue
        print('Reading: ', path, end='\r')
        
        # iterate lines in file
        for title, categories, intro, body in yield_docs_path(path):
            yield path, title, categories, intro, body


if __name__ == '__main__':
    
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filepath>")
        exit(-1)
    
    for title, categories, intro, body in yield_docs_path(sys.argv[1]):
        print(f"Title: {title}")
        print(f"Categories: {categories}")
        print(f"Intro: {intro}")
        print(f"Body: {body}")
        print("-" * 40)

    
    