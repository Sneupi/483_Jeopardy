import numpy as np
from retrievers import JeopardyBM25, JeopardyDPR
import utils


QUESTIONS = [_ for _ in utils.yield_questions('assets/questions.txt')] # load generator as list
IR = [JeopardyBM25('.index.bm25s'), JeopardyDPR('.index.faiss')]
K = 100


def construct_query(category, clue):
    '''Construct query as f"{category}: {clue}"'''
    return f"{category}: {clue}"


def eval_precision_at_1():
    
    for ir in IR:
        
        p_at_1 = 0.0
        
        for category, clue, answers in QUESTIONS:
            
            titles = ir.search(construct_query(category, clue), k=K)
            
            # Consider all aliases of top result
            if set(answers).intersection(titles[0]):
                p_at_1 += 1.0
        
        print(f'P@1 ({type(ir).__name__}): {(p_at_1/float(len(QUESTIONS))):.4}')


def eval_mrr():
    
    for ir in IR:
        
        mrr = []
        
        for category, clue, answers in QUESTIONS:
            
            titles = ir.search(construct_query(category, clue), k=K)
            
            rank = 0.0
            for i, aliases in enumerate(titles):
                if set(aliases).intersection(answers):
                    rank = 1.0 / (i + 1)
                    break
                
            mrr.append(rank)
        
        print(f"MRR@{K} ({type(ir).__name__}): {np.mean(mrr):.4}")
        
        
if __name__ == "__main__":
    eval_mrr()
    eval_precision_at_1()