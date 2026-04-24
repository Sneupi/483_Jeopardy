import pytest
import numpy as np
import retrievers
import utils

QUESTIONS = [
    (category, clue, answers) 
    for category, clue, answers 
    in utils.yield_questions('assets/questions.txt')
]

IR = retrievers.JeopardyBM25('.index.bm25s')
K = 100

@pytest.mark.parametrize("category, clue, answers", QUESTIONS)

def test_topK(category, clue, answers):
    titles = IR.search(f"{category}: {clue}", k=K) # list of lists
    flattened = [item for sublist in titles for item in sublist]
    assert set(answers).intersection(flattened)

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
    assert mean_mrr > 0.40, f"MRR@{K}: {mean_mrr}"