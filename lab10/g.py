import csv

data = [
    ["Sagima", "+71234567890"],
    ["Adina", "+79876543210"],
    ["Nazi", "+75551234567"]
]

with open("phonebook.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV файл 'phonebook.csv' создан!")