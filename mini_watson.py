import os
import re
import argparse
from whoosh.index import create_in, open_dir, exists_in
from whoosh.fields import *
from whoosh import qparser, analysis, query
import wiki_parser

class Watson:
    '''Mini-implementation of IBM Watson, 
    a Question Answer (QA) system designed 
    to respond to hints for the game Jeopardy'''
    
    def __init__(self, corpus, index):
        
        # Check collection exists
        if not os.path.isdir(corpus):
            print(f"Directory \"{corpus}\" not found.")
            exit(1)
            
        # If index exists, avoid creation
        if exists_in(index):
            self.ix = open_dir(index)
            return
        
        # Load Whoosh
        os.makedirs(index, exist_ok=True)
        # stem ir terms (docs & queries),
        # use unbound cache for index speed
        stem_ana = analysis.StemmingAnalyzer(cachesize=-1) 
        schema = Schema(title=ID(stored=True), 
                        body=TEXT(analyzer=stem_ana),
                        path=ID(stored=True))
        self.ix = create_in(index, schema)
        # Use whole gigabyte of RAM (across 
        # 4 processes) to speed up indexing 
        writer = self.ix.writer(procs=4, multisegment=True, limitmb=256)
        
        # Add documents, partitioned by txt file, in collection dir
        for file in os.listdir(corpus):
            
            # For each txt in dir
            if file.endswith('.txt'):
                
                # Add docs in txt
                path = os.path.join(corpus, file)
                print('* Indexing:', path)
                for document in wiki_parser.iterate_entries(path):
                    writer.add_document(title=document['title'], 
                                        path=path, 
                                        body=document['body'])
        
        # Commit docs to whoosh index
        print('Comitting documents to index...',end='')
        writer.commit()
        print('done!')

        
    def run_query(self, user_query):
        '''Returns list of guesses (title, path) based on hint'''
        with self.ix.searcher() as searcher:

            # check query against all fields, 
            # using schema (stems query terms),
            # matching one or more terms (OrGroup),
            # where all term variations are explored
            
            parser = qparser.QueryParser("body", 
                                         self.ix.schema, 
                                         group=qparser.OrGroup.factory(0.9),
                                         termclass=query.Variations)
            
            whoosh_query = parser.parse(user_query)
            
            return [{'title':res['title'], 'path':res['path']} for res in searcher.search(whoosh_query)]
    
    def guess(self, query):
        '''Returns best guess based on hint'''
        return self.run_query(query)[0]['title']
        
def main(corpus, index):
    ir = Watson(corpus, index)

    while True:
        
        # Process query
        query = input('Query: ').strip()
        if query == 'exit':
            break
        results = ir.run_query(query)
        
        # Print results
        for i, res in enumerate(results):
            print(i+1)
            print('  ' + res['title'])
            print('  ' + res['path'])
        print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("CORPUS",
                        help="Path to directory with the corpus")
    parser.add_argument("INDEX",
                        help="Path to directory with the index")
    args = parser.parse_args()
    main(args.CORPUS, args.INDEX)