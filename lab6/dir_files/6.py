import string  
def letter_files(): 
    for letter in string.ascii_uppercase: 
        filename = f"{letter}.txt" 
        with open(filename, "w") as file: 
            file.write(f"Это файл {filename}\n") 
    print("file A.txt to Z.txt is ready")  
letter_files()


