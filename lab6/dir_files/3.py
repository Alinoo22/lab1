import os
def items(path):
    if os.path.exists(path):
        print("exists!")

    file = os.path.basename(path)
    print("Имя файла: ", file)
    directory = os.path.dirname(path)
    print("Имя папки: ", directory)

path = input("Введите путь: ")
items(path)