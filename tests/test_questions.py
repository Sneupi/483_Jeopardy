import pytest
from retrievers import JeopardyBM25, JeopardyDPR
import utils
import eval
from transformers import AutoModel, AutoTokenizer


MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
q_tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
q_model = AutoModel.from_pretrained(MODEL_NAME)
q_model.eval()

DPR = JeopardyDPR('.index.faiss', '.titles.pkl', q_tokenizer, q_model)
BM25 = JeopardyBM25('.index.bm25s')


@pytest.mark.parametrize("QUESTION", [_ for _ in utils.yield_questions('assets/questions.txt')])


# def test_top1_dpr(QUESTION: tuple[str, str, list[str]]):
#     category, clue, answers = QUESTION
#     # list of lists
#     titles = DPR.search(eval.construct_query(category, clue), k=1)
#     # check if answer in aliases of top guess
#     assert set(answers).intersection(titles[0]), f'{type(DPR).__name__}: {answers} not in top guess {titles[0]}'

# def test_topK_dpr(QUESTION: tuple[str, str, list[str]]):
#     k=10
#     category, clue, answers = QUESTION
#     # list of lists
#     titles = DPR.search(eval.construct_query(category, clue), k=k)
#     # check if answer in aliases
#     flattened = [item for sublist in titles for item in sublist]
#     assert set(answers).intersection(flattened), f'{type(DPR).__name__}: {answers} not in top K={k}'

def test_top1_bm25(QUESTION: tuple[str, str, list[str]]):
    category, clue, answers = QUESTION
    # list of lists
    titles = BM25.search(eval.construct_query(category, clue), k=1)
    # check if answer in aliases of top guess
    assert set(answers).intersection(titles[0]), f'{type(BM25).__name__}: {answers} not in top guess {titles[0]}'