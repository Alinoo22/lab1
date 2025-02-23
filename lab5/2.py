import re
with open('row.txt', 'r', encoding='utf-8') as file:
    txt = file.read()
word = r'ab{2,3}' 

matches = re.findall(word, txt) 
if matches:
    print("GOOD:", matches) 
else:
    print("NOO")


