def is_palyndrom(text):
    return text == text[::-1]

text = input("Введите слово: ")
if is_palyndrom(text):
    print("TRUE")
else:
    print("FALSE")
    