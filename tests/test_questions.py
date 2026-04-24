import pytest
import numpy as np
import retrievers
import utils
import os

BM25S_INDEX = '.index.bm25s'
CORPUS = '.wiki'

if not os.path.exists(BM25S_INDEX):
    retrievers.JeopardyBM25.create_index(BM25S_INDEX, CORPUS)

QUESTIONS = [
    (category, clue, answers) 
    for category, clue, answers 
    in utils.yield_questions('assets/questions.txt')
]

IR = retrievers.JeopardyBM25(BM25S_INDEX)
K = 100

@pytest.mark.parametrize("category, clue, answers", QUESTIONS)

def test_top1(category, clue, answers):
    titles = IR.search(f"{category}: {clue}", k=K) # list of lists
    # flattened = [item for sublist in titles for item in sublist] # all titles for all results in top K
    assert set(answers).intersection(titles[0])

def test_MRR():
    
    scores_mrr = []
    
    for category, clue, answers in QUESTIONS:
        
        titles = IR.search(f"{category}: {clue}", k=K) # list of lists
        
        rank = 0.0
        for i, aliases in enumerate(titles):
            if set(aliases).intersection(answers):
                rank = 1.0 / (i + 1)
                break
            
        scores_mrr.append(rank)
    
    mean_mrr = np.mean(scores_mrr)
    assert mean_mrr > 0.5, f"MRR@{K}: {mean_mrr}"