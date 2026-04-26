from retrievers import JeopardyBM25

def construct_query(category, clue):
    return f"{category}: {clue}"


def rank(response: list[list[str]], answers: list[str]):
    for i, aliases in enumerate(response):
        if set(answers).intersection(aliases):
            return i + 1
    return 0


def eval_p_at_1(ir: JeopardyBM25, questions: list[tuple[str, str, list[str]]], k: int):
    pat1 = 0
    for category, clue, answers in questions:
        titles = ir.search(construct_query(category, clue), k=k)
        if set(answers).intersection(titles[0]):
            pat1 += 1
    pat1 /= float(len(questions))
    print(f"P@1 ({type(ir).__name__}): {pat1:.4}")



def eval_mrr(ir: JeopardyBM25, questions: list[tuple[str, str, list[str]]], k: int):
    mrr = 0.0
    for category, clue, answers in questions:
        titles = ir.search(construct_query(category, clue), k=k)
        r = rank(titles, answers)
        if r: mrr += 1.0 / r
    mrr /= float(len(questions))
    print(f"MRR@{k} ({type(ir).__name__}): {mrr:.4}")