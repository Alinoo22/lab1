import shutil
import os
files = ["A.txt", "B.txt", "C.txt"]  
for item in files:
    if os.path.exists(item): 
        shutil.copy(item, f"Copy_of_{item}")  
        print(f"Файл {item} скопирован!")
    else:
        print(f"Файл {item} не найден!")
