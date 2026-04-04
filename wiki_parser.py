import re
import mwparserfromhell

def _clean_body(body):
        '''Crude cleaning of body from wiki syntax'''
        mediawiki_cleaned = mwparserfromhell.parse(body).strip_code(normalize=True, collapse=True) 
        return re.sub(r'(\[tpl\].*?\[/tpl\]|\[/?tpl\]|[^\s\n]*\|[^\s\n]*)|\[/?ref\]|}}', '', mediawiki_cleaned, flags=re.DOTALL)
        
def iterate_entries(path):
    '''Iterate Wiki entries contained in singular textfile'''
    
    title_pattern = re.compile(r"^\[\[([^\n:]*)\]\]$")
    title = None
    body = []
        
    with open(path) as file:
        for line in file:
            new_title = title_pattern.match(line.strip())
            
            # new entry found
            if new_title:
                line = new_title.group(1)
                
                # if older entry stored, spit out 
                if title is not None:
                    yield {'title':title, 'body':_clean_body(''.join(body))}
                    
                # track new entry
                title = line
                body = []
            
            # else add to body under title
            elif title and line:
                body.append(line)
                
        # EOF, yield last entry
        if title is not None:
            yield {'title':title, 'body':_clean_body(''.join(body))}

# Test print for a set of files
if __name__ == "__main__":
    
    import sys
    
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <wikifile1> [wikifile2 ...]")
    
    for i in range(1, len(sys.argv)):
        
        print(f"\033[1;32m{sys.argv[i]}\033[0m")

        for entry in iterate_entries(sys.argv[i]):
            pass
            print(entry['title'])
            print(entry['body'])
            print('-'*80)    
     