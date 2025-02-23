import re
with open('row.txt', 'r', encoding='utf-8') as file:
    txt = file.read().strip() 
def snaketo_camel(txt):
    wordd = txt.split('_') 
    new = '' 
    for word in wordd:
        new += word.capitalize() 
    return new  

print(snaketo_camel(txt))  
