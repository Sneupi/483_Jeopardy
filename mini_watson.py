import os
import re
import argparse
from whoosh.index import create_in, open_dir, exists_in
from whoosh.fields import *
from whoosh import qparser, analysis, query

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
        stem_ana = analysis.StemmingAnalyzer() # stem all terms (docs & queries)
        schema = Schema(title=TEXT(stored=True, analyzer=stem_ana), 
                        body=TEXT(analyzer=stem_ana),
                        path=ID(stored=True))
        self.ix = create_in(index, schema)
        writer = self.ix.writer()
        
        # Add documents, partitioned by txt file, in collection dir
        for file in os.listdir(corpus):
            
            # For each txt in dir
            if file.endswith('.txt'):
                
                # Add docs in txt
                path = os.path.join(corpus, file)
                for title, body in self.parse_document(path):
                    print(title) # DEBUGGING
                    # print("\n\nADDING\n" + title + "\n\t" + body) # DEBUGGING
                    writer.add_document(title=title, body=body, path=path)
        
        # Commit docs to whoosh index
        writer.commit()

    def parse_document(self, path):
        '''Yields title, body pairs from text file'''
        
        # conservative matching, specific exclusion 
        # of matching File and Image embeds
        title_pattern = re.compile(r"^\[\[(?!(?:File:|Image:)).*\]\]$")
        
        title = None
        body = []
            
        with open(path) as f:
            for line in f:
                line = line.strip()
                
                # if title found
                if title_pattern.match(line):
                    
                    # spit out last entry (if avail)
                    if title is not None:
                        yield title, self.filter_mediawiki(body)
                        
                    # track new entry
                    title = line[2:-2]
                    body = []
                
                # else add to body under title
                elif title and line:
                    body.append(line)
                    
            # EOF, yield last entry
            if title is not None:
                yield title, self.filter_mediawiki(body)
    
    def filter_mediawiki(self, text):
        '''Filter most common MediaWiki syntax from text'''
        
        if isinstance(text, list):
            text = " ".join(t.strip() for t in text)
        assert isinstance(text, str)
        
        # remove table delimiters e.g. [tpl]tag1=thing1|tag2=thing2[/tpl] -> thing1 thing2
        text = re.sub(r'\[tpl\](.*?)\[\/tpl\]', lambda m: ' '.join((v.split('=')[1] if len(v.split('=')) > 1 else v) for v in m.group(1).split('|')), text, flags=re.DOTALL)
        
        # remove all other blocks e.g. [BLOCK]something[/BLOCK] -> something
        text = re.sub(r'\[.*\](.*?)\[\/.*\]', r' \1 ', text, flags=re.DOTALL)

        # remove embeds e.g. [[EMBED:something]] -> something
        text = re.sub(r'\[\[(?:.*?):(.*?)\]\]', r' \1 ', text, flags=re.DOTALL)

        # remove header markdown e.g. ==something== -> something
        text = re.sub(r'=+(.+?)={2,}', r' \1 ', text)
        
        return text
        
    def run_query(self, user_query):
        '''Returns list of guesses (title, path) based on hint'''
        with self.ix.searcher() as searcher:

            # check query against all fields, 
            # using schema (stems query terms),
            # matching one or more terms (OrGroup),
            # where all term variations are explored
            
            parser = qparser.MultifieldParser(fieldnames=["title", "body"], 
                                              schema=self.ix.schema, 
                                              group=qparser.OrGroup.factory(0.9),
                                              termclass=query.Variations)
            
            whoosh_query = parser.parse(user_query)
            
            return [(res['title'], res['path']) for res in searcher.search(whoosh_query)]
    
    def guess(self, query):
        '''Returns best guess based on hint'''
        return self.run_query(query)[0][0]
        
def main(corpus, index):
    ir = Watson(corpus, index)

    while True:
        
        # Process query
        query = input('Query: ').strip()
        if query == 'exit':
            break
        results = ir.run_query(query)
        
        # Print results
        for i, (title, path) in enumerate(results):
            print(i+1)
            print('  ' + title)
            print('  ' + path)
        print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("CORPUS",
                        help="Path to directory with the corpus")
    parser.add_argument("INDEX",
                        help="Path to directory with the index")
    args = parser.parse_args()
    main(args.CORPUS, args.INDEX)