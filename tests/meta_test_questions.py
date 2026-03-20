# Metaprogram used to generate 'test_questions.py' from 'questions.txt'

with open("questions.txt") as q_file, open("test_questions.py", "w") as py_file:
    
    py_file.write("import mini_watson\n")
    py_file.write("ir = mini_watson.Watson(\"wiki\")\n")
    
    q_content = q_file.read().split('\n\n')
    q_list = [q.strip() for q in q_content if q.strip()]
    
    for i, q in enumerate(q_list):
        category, question, answer = q.split('\n')
        
        py_file.write(f"\ndef test_question_{i+1}():\n")
        py_file.write(f"\tresponse = ir.guess(\"{question.replace('"', '\\"')}\")\n")
        py_file.write(f"\tassert response == \"{answer}\"\n")
    
    
    
        
        
        
        
        
        
        