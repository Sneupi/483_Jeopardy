# Metaprogram used to generate 'questions.py' from 'questions.txt'

def main():
    
    with open("questions.txt") as q_file, open("questions.py", "w") as py_file:
        
        py_file.write("QA = [\n")
        
        q_content = q_file.read().split('\n\n')
        q_list = [q.strip() for q in q_content if q.strip()]
        q_strings = []
        
        for cqa in q_list:
            category, question, answer = cqa.split('\n')
            
            query = "\"" + category.replace('"', '\\"') + ", " + question.replace('"', '\\"') + "\""
            
            answer = answer.split('|') # list of answers divided by '|' (or)
            
            q_strings.append(f"\t({query}, {answer})")
            
        py_file.write(',\n'.join(q_strings))
        py_file.write("\n]\n")
        
if __name__ == "__main__":
    main()
        