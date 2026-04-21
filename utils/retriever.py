import bm25s
import os
import spacy
import Stemmer

# Run 'python -m spacy download en_core_web_sm' in your terminal first
nlp = spacy.load("en_core_web_sm", disable=["lemmatizer", "parser"])

# TODO - Implement reranking for near-misses (in top K, but not #1), maybe via AI

class Retriever:
    def __init__(self, index_dir):
        '''
        Util class (wrapper) for bm25s BM25 class. 
        Handles index loading and retrieval.
        '''
        
        assert os.path.exists(index_dir), f"Directory not found \"{index_dir}\""
        
        self.retriever = bm25s.BM25.load(index_dir, load_corpus=True)
        stemmer = Stemmer.Stemmer("english")
        self.tokenizer = bm25s.tokenization.Tokenizer(stemmer=stemmer)
        self.tokenizer.load_vocab(index_dir)
        
    def _refine_query(self, query: str):
        '''
        Returns Jeopardy query by keeping 
        only descriptive content words
        '''
        category, query = query.split(',', 1)
        doc = nlp(query)
        
        # 1. Extract Named Entities (e.g., "Abraham Lincoln", "1865")
        # Entities are crucial for Jeopardy clues
        entities = [ent.text for ent in doc.ents]
        
        # 2. Filter tokens by Part-of-Speech
        # We keep only descriptive content words
        pos_filtered = [
            token.text for token in doc 
            if token.pos_ in {"NOUN", "PROPN", "ADJ"} and not token.is_stop
        ]
        
        # 3. Combine and Deduplicate
        # We give "Double Weight" to entities by adding them twice to the string
        # to ensure BM25 prioritizes exact entity matches
        refined_tokens = [category] + pos_filtered + entities
        
        return ' '.join(refined_tokens)
        
    def run_query(self, query, k):
        '''
        Wrapper of bm25s BM25.retrieve(). 
        Performs tokenization on input query.
        '''
        
        query_tokens = self.tokenizer.tokenize([self._refine_query(query)], update_vocab=False)
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