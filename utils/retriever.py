import bm25s
import os

# TODO - Implement reranking for near-misses (in top K, but not #1), maybe via AI

class Retriever:
    def __init__(self, index_dir):
        '''
        Util class (wrapper) for bm25s BM25 class. 
        Handles index loading and retrieval.
        '''
        
        assert os.path.exists(index_dir), f"Directory not found \"{index_dir}\""
        
        self.retriever = bm25s.BM25.load(index_dir, load_corpus=True)
        self.tokenizer = bm25s.tokenization.Tokenizer(splitter=lambda x: x.split())
        self.tokenizer.load_vocab(index_dir)
        
    def run_query(self, query, k):
        '''
        Wrapper of bm25s BM25.retrieve(). 
        Performs tokenization on input query.
        '''
        
        query_tokens = self.tokenizer.tokenize([query], update_vocab=False)
        output = results, scores = self.retriever.retrieve(query_tokens, k=k)
        return output


def main(index_dir):    
    
    ir = Retriever(index_dir)
        
    while True:
        
        query = input('Query: ').strip()
        if query == 'exit':
            break
        
        results, scores = ir.run_query(query, 10)
        
        for i in range(results.shape[1]):
            doc, score = results[0, i], scores[0, i]
            print(f"{f"({score:.2f})":>8} {i+1:>2}: {doc['title']}") # doc['text'] for bodies
        
        
if __name__ == "__main__":
    
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <index_dir>")
        exit(-1)
        
    # load index dir
    main(sys.argv[1])