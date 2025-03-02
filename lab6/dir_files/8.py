import os 
path = "A.txt"
if os.path.exists(path):  
    os.remove(path)  
    print(f"Файл {path} удалён!")  
else:
    print(f"Файл {path} не найден!") 
