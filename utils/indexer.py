# Modification on the following example:
# https://github.com/xhluca/bm25s/blob/main/examples/index_nq.py

from pathlib import Path
import bm25s
import Stemmer
import os
import re

# TODO - Cleaning the bodies of MediaWiki syntax and other non-natural language before indexing

def yield_docs(corpus_dir):
    '''
    Yields wiki entries contained in text 
    files contained in corpus directory
    '''
    
    title_pattern = re.compile(r"^\[\[([^\n:]*)\]\]$")
    title = None
    body = []
    
    # iterate files in dir
    for f in os.listdir(corpus_dir):                
        path = os.path.join(corpus_dir, f)
        
        # skip all subdirs
        if os.path.isdir(path): continue
        print('Reading: ', path, end='\r')
        
        # iterate lines in file
        with open(path) as file:
            for line in file:
                
                # collect to entries, yielding
                match = title_pattern.match(line)
                if match:
                    if title:
                        yield path, title, ''.join(body)
                    title = match.group(1)
                    body = []
                else:
                    body.append(line)
                    
    # EOF, yield last entry
    if title:
        yield path, title, ''.join(body)
    

def create_index(index_dir, dataset_dir):
    os.mkdir(index_dir)
    
    # load entire corpus to mem (OK for our ~1GB raw text corpus)
    corpus_records = [
        {"id": i, "path": p, "title": t, "text": b} for i, (p, t, b) in enumerate(yield_docs(dataset_dir))
    ]
    corpus_lst = [r["title"] + " " + r["text"] for r in corpus_records]

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