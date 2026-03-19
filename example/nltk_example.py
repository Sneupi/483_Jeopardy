import re
import nltk
nltk.download('punkt_tab')

# lets get the set of tokens & terms
tokens = set()
terms = set()

# open a wiki file
with open("wiki-example.txt") as file:
    content = file.read()
    
    # iterate each title, body
    for match in re.finditer(r'\[\[(.+?)\]\](.*?)(?=\[\[|$)', content, re.DOTALL):
        
        title = match.group(1).strip()
        body = match.group(2).strip()
        
        tokens.update(set(nltk.word_tokenize(body)))

tokens = sorted(list(tokens))
terms = [nltk.PorterStemmer().stem(t) for t in tokens]

# for demo, print token-term pairs
max_len_tok = max([len(t) for t in tokens])
for tok,term in zip(tokens,terms):
    print(f"{tok:<{max_len_tok}} -> {term}")