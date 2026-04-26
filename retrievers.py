from abc import ABC, abstractmethod
import os
import Stemmer
import bm25s
import utils
import re
import torch
from transformers import AutoTokenizer, AutoModel
import faiss
import pickle
import collections


class Jeopardy(ABC):
    @abstractmethod
    def search(self, query: str, k: int):
        '''Returns top K answers based on query'''
        pass

class JeopardyBM25(Jeopardy):
    def __init__(self, index_path):
        assert os.path.exists(index_path), f"BM25S index not found \"{index_path}\""
        self.retriever = bm25s.BM25.load(index_path, load_corpus=True)
        stemmer = Stemmer.Stemmer("english")
        self.tokenizer = bm25s.tokenization.Tokenizer(stemmer=stemmer)
        self.tokenizer.load_vocab(index_path)
        
    def search(self, query, k):
        # refine query tailoring for jeopardy prompts
        refined_clue = utils.refine_clue(query)
        # tokenize refined query
        query_tokens = self.tokenizer.tokenize([refined_clue], update_vocab=False)
        # search
        results, scores = self.retriever.retrieve(query_tokens, k=k)
        return [results[0, i]['titles'] for i in range(results.shape[1])]
    
    @staticmethod
    def create_index(index_dir, corpus_dir):
        os.mkdir(index_dir)
        
        wiki_titles = []
        wiki_redirects =  collections.defaultdict(lambda: []) # Ignore redirects, but store as aliases
        wiki_content = []

        # load entire corpus to mem (OK for our ~1GB text corpus)
        for title, content in utils.yield_wiki_corpus(corpus_dir):
            
            # clean raw content
            content = utils.clean_mediawiki(content)
            
            # if alias, track but dont actually index
            found = re.search(r'^\s*#redirect\s+(.*?)$', content, re.IGNORECASE|re.MULTILINE)
            if found:
                real_page = found.group(1).strip()
                wiki_redirects[real_page].append(title)
                continue
            
            # keep hold of title->content mapping
            wiki_titles.append(title)
            wiki_content.append(content)

        # tokenization step
        stemmer = Stemmer.Stemmer("english")
        tokenizer = bm25s.tokenization.Tokenizer(stemmer=stemmer)
        corpus_tokens = tokenizer.tokenize(wiki_content, return_as="tuple")

        # indexing & bm25 calc
        # (these k1 and b perform best for the provided corpus, 
        # favoring short queries & reducing wiki length penalty) 
        saved_corpus = [{'titles': [title] + wiki_redirects[title]} for title in wiki_titles]
        retriever = bm25s.BM25(corpus=saved_corpus, backend="numba", k1=1.1, b=0.4, method='lucene')
        retriever.index(corpus_tokens)
        
        # save for reuse
        retriever.save(index_dir)
        tokenizer.save_vocab(index_dir)
        tokenizer.save_stopwords(index_dir)
        print(f"Saved the index to {index_dir}.")
        
        # get memory usage (expected usage ~5GB)
        mem_use = bm25s.utils.benchmark.get_max_memory_usage()
        print(f"Peak memory usage: {mem_use:.2f} GB")


class JeopardyDPR(Jeopardy):
    def __init__(self, index_path, titles_path, redirects_path, tokenizer, model):
        
        self.tokenizer = tokenizer
        self.model = model.to('cuda')
        self.model.eval()
        
        self.index = faiss.read_index(index_path)
        
        self.titles = utils.load_pickle(titles_path)
        self.redirects = utils.load_pickle(redirects_path)
        
    def search(self, query, k):
        
        inputs = self.tokenizer(query, return_tensors="pt").to('cuda')
        with torch.no_grad():
            embedding = self.model(**inputs).pooler_output.cpu().numpy()
        
        distances, indices = self.index.search(embedding, k)
        
        return [self.titles[int(i)] for i in indices[0]]


if __name__ == "__main__":
    
    model_name = 'sentence-transformers/all-MiniLM-L6-v2'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    model.eval()
    
    ir = JeopardyDPR('.index.faiss', '.titles.pkl', tokenizer, model)
    
    while True:    
        query = input('Query: ').strip()
        if query == 'exit':
            break
        
        titles = ir.search(query, 10)
        
        print('\n\n'.join([f'{i:>2}:{t}' for i, t in enumerate(titles)]))