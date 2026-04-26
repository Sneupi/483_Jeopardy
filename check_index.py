
# Quickly checks that all answers are indexed and 
# formatted correctly in BM25 index such that they 
# are findable and appear as-expected for unit tests
   
import json
import utils

with open(".index.bm25s/corpus.jsonl") as file:
    all_findable_titles = []
    
    for line in file:
        doc_record = json.loads(line)
        all_findable_titles.extend(doc_record['title'])
    
    for category, clue, answers in utils.yield_questions('assets/questions.txt'):
        if not set(answers).intersection(all_findable_titles):
            print("Not findable",answers)
        