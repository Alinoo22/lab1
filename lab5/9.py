import re
with open('row.txt', 'r', encoding='utf-8') as file:
    txt = file.read().strip() 
new = re.sub(r'(?<!^)([A-Z])', r' \1', txt).strip()
if new:
    print("GOOD:", new)
else:
    print("NOOOO")
