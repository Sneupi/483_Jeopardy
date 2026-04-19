
# Quickly checks that all answers are indexed and 
# formatted correctly in BM25 index such that they 
# are findable and appear as-expected for unit tests
   
import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.questions import QA
with open(".bm25s/corpus.jsonl") as corpus:
    
    # Get all titles in corpus
    pattern = re.compile(r'.*?"title":"(.*?)".*?')
    titles = [pattern.match(line).group(1) for line in corpus if pattern.match(line)]
        
    # Get titles that are answers
    answers = [a for q,a in QA]
    
    [print('NOT INDEXED', ans) if not set(ans).intersection(titles) else None for ans in answers]