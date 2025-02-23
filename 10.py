import re

with open ('row.txt', 'r', encoding = 'utf-8') as file:
  txt = file.read().strip()
def camelto_snake(txt):
  result = re.sub(r'(?<!^)([A-Z])', r'_\1', txt).lower()
  return result.lstrip('_')


print(camelto_snake(txt)) 
