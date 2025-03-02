def count(text):
    count_upper = 0
    count_lower = 0
    for char in text:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    return count_upper , count_lower

text= input("Введите текст: ")
upper, lower = count(text)
print("UPPER:",upper)
print("LOWER:", lower)