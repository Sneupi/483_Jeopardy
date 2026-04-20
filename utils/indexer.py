# Modification on the following example:
# https://github.com/xhluca/bm25s/blob/main/examples/index_nq.py

import bm25s
import Stemmer
import os
from parser import yield_docs_corpus

def create_index(index_dir, dataset_dir):
    os.mkdir(index_dir)
    
    # load entire corpus to mem (OK for our ~1GB raw text corpus)
    corpus_records = [
        {
            "id": i, 
            "path": pth, 
            "title": ttl, 
            "categories": cat, 
            "intro": itr, 
            "body": bdy
        } 
        for i, (pth, ttl, cat, itr, bdy) 
        in enumerate(yield_docs_corpus(dataset_dir))
    ]
    
    # Duplicate sections, boosting it's relative significance on the document
    corpus_lst = [' '.join([r["title"]]*10+r["categories"]*5+[r["intro"]]*2+[r["body"]]) for r in corpus_records]

    # tokenization step
    stemmer = Stemmer.Stemmer("english")
    tokenizer = bm25s.tokenization.Tokenizer(stemmer=stemmer)
    corpus_tokens = tokenizer.tokenize(corpus_lst, return_as="tuple")

    # indexing & bm25 calc
    retriever = bm25s.BM25(corpus=corpus_records, backend="numba")
    retriever.index(corpus_tokens)
    
    # save for reuse
    retriever.save(index_dir)
    tokenizer.save_vocab(index_dir)
    tokenizer.save_stopwords(index_dir)
    print(f"Saved the index to {index_dir}.")
    
    # get memory usage (expected usage ~6GB)
    mem_use = bm25s.utils.benchmark.get_max_memory_usage()
    print(f"Peak memory usage: {mem_use:.2f} GB")


if __name__ == "__main__":
    
    import sys
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <index_dir> <dataset_dir>")
        exit(-1)
            
    # create index from wiki
    create_index(index_dir=sys.argv[1], dataset_dir=sys.argv[2])