import re
with open ('row.txt', 'r', encoding = 'utf-8')as file:
    txt = file.read()
word = r'a.*b'
match = re.findall(word,txt)
if match:
    print("GOOD: ", match)
else:
    print("NOOO")