import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest
import numpy as np
from utils.retriever_hybrid import BM25TfidfRetriever
from questions import QA

IR = BM25TfidfRetriever(".bm25s")
K = 100

@pytest.mark.parametrize("query, target_titles", QA)

def test_topK_bm25tfidf(query, target_titles):
    res, scr = IR.run_query(query, k=K)
    result_titles = [res[0, i]['title'] for i in range(res.shape[1])]
    assert set(target_titles).intersection(result_titles), f"{target_titles} not in top K={K} results"

def test_top_guess_bm25tfidf(query, target_titles):
    res, scr = IR.run_query(query, k=K)
    result_titles = [res[0, i]['title'] for i in range(res.shape[1])]
    assert result_titles[0] in target_titles

def test_MRR_bm25tfidf():
    
    scores_mrr = []
    
    for query, target_titles in QA:
        
        res, scr = IR.run_query(query, k=K)
        result_titles = [res[0, i]['title'] for i in range(res.shape[1])]
        
        rank = 0.0
        for result in result_titles:
            if result in target_titles:
                rank = 1.0 / (result_titles.index(result) + 1)
                break
            
        scores_mrr.append(rank)
    
    mean_mrr = np.mean(scores_mrr)
    
    # Set quality bar
    assert mean_mrr > 0.7, f"MRR @ K={K}: {mean_mrr}"
