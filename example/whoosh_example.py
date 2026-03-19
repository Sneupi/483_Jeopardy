import os
import re
from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser

# NOTE: no tokenization, normalization (see nltk_example.py)

# Create whoosh index if not created
index_dir = "index"
if not os.path.exists(index_dir):
    print('Creating whoosh index...', end='')
    os.makedirs(index_dir)
    
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    ix = create_in(index_dir, schema)
    writer = ix.writer()

    with open("wiki-example.txt") as file:
        content = file.read()
        documents = []
        for match in re.finditer(r'\[\[(.+?)\]\](.*?)(?=\[\[|$)', content, re.DOTALL):
            writer.add_document(title=match.group(1).strip(), 
                                path=u"/a",
                                content=match.group(2).strip())
    writer.commit()
    print('created!')

# Search user queries
ix = open_dir(index_dir)
with ix.searcher() as searcher:
    
     while True:
        user_input = input('Query: ').strip()
        
        if user_input == 'exit':
            break
        
        query = QueryParser("content", ix.schema).parse(user_input)
        results = searcher.search(query)
        for hit in results:
            print(hit)