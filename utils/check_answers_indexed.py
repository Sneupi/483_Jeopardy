
# Quickly checks that all answers are indexed and 
# formatted correctly in BM25 index such that they 
# are findable and appear as-expected for unit tests
   
import re
from indexer import yield_docs
with open(".bm25s/corpus.jsonl") as corpus, open("tests/questions.txt") as q_file:
    
    # Get all titles in corpus
    pattern = re.compile(r'.*?"title":"(.*?)".*?')
    titles = [pattern.match(line).group(1) for line in corpus if pattern.match(line)]
        
    # Get titles that are answers
    q_content = q_file.read().split('\n\n')
    q_list = [q.strip() for q in q_content if q.strip()]
    answers = [q.split('\n')[2] for q in q_list]
    
    def exists_in(ans: str, titles: list):
        # Check all variations of answer
        ans_splt = ans.split('|')
        for splt in ans_splt:
            if splt in titles: return True
        return False
    
    [print("NOT EXISTS", ans) if not exists_in(ans, titles) else print('EXISTS', ans) for ans in answers]