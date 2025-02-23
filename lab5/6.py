import re
with open ('row.txt', 'r', encoding = 'utf-8')as file:
     txt = file.read()
text = re.sub(r'[,\.\s]',':',txt)
if text:
     print("GOOD: ", text)
else:
     print("NOOOOO")