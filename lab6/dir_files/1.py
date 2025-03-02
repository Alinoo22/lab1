import os
def list(path):
    try:
        items = os.listdir(path)
        only_dir = [item for item in items if os.path.isdir(os.path.join(path,item))]
        only_file = [item for item in items if os.path.isfile(os.path.join(path,item))]
        print("Папки")
        print(only_dir)
        print("\n Файлы")
        print(only_file)
        print("\n Всеее ")
        print(items)
    except FileNotFoundError:
        print("Ошибка,файл не найдена!")
    except PermissionError:
        print("Ошибка,у вас нету разрешения")
path = input("Введите путь к файлу: ")
list(path)

