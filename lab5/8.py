import re
with open ('row.txt', 'r', encoding = 'utf-8')as file:
    txt = file.read()
text = re.split(r'(?=[A-Z])', txt)

if text:
    print("GOOD: ",text)
else:
    print("NOOOO")