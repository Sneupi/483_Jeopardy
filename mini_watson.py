import os
import argparse

class Watson:
    '''Mini-implementation of IBM Watson, 
    a Question Answer (QA) system designed 
    to respond to hints for the game Jeopardy'''
    
    def __init__(self, corpus):
        if not os.path.exists(corpus):
            print(f"Directory \"{corpus}\" not found.")
            exit(1)
        # TODO indexing
    
    def run_query(self, query):
        '''Returns list of guesses based on hint'''
        results = [str('<wiki_title>')]
        # TODO matching
        return results
    
    def guess(self, query):
        '''Returns best guess based on hint'''
        return self.run_query(query)[0]
        
def main(corpus):
    ir = Watson(corpus)

    while True:
        query = input('Query: ').strip()
        if query == 'exit':
            break
        results = ir.run_query(query)
        print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("CORPUS",
                        help="Path to directory with the corpus")
    args = parser.parse_args()
    main(args.CORPUS)