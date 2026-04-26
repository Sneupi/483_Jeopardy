import pytest
from retrievers import JeopardyBM25
import utils
import eval

IR = JeopardyBM25('.index.bm25s')
K = 1

@pytest.mark.parametrize("QUESTION", [_ for _ in utils.yield_questions('assets/questions.txt')])
    
def test_bm25_topK(QUESTION: tuple[str, str, list[str]]):
    category, clue, answers = QUESTION
    
    # list of lists
    titles = IR.search(eval.construct_query(category, clue), k=K)
    
    # check if answer in aliases
    flattened = [item for sublist in titles for item in sublist]
    assert set(answers).intersection(flattened), f'{type(IR).__name__}: {answers} not in top K={K}: {flattened}'