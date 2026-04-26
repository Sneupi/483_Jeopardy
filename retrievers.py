import os
import Stemmer
import bm25s
import utils
import re
import collections


class JeopardyBM25:
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
        return [results[0, i]['title'] for i in range(results.shape[1])]
    
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
        saved_corpus = [{'title': [title] + wiki_redirects[title]} for title in wiki_titles]
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
        

if __name__ == "__main__":
    
    ir = JeopardyBM25('.index.bm25s')
    
    while True:    
        query = input('Query: ').strip()
        if query == 'exit':
            break
        
        titles = ir.search(query, 10)
        
        print('\n\n'.join([f'{i:>2}:{t}' for i, t in enumerate(titles)]))