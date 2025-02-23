import re
with open('row.txt','r', encoding = 'utf-8') as file:
  txt = file.read()
word = r'[A-Z][a-z]+'
matches = re.findall(word, txt)
if matches:
    print("GOOD: ", matches)
else:
    print("NOOO")