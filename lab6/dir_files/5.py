filename = "text.txt"
text = ("Radiohead самая лучшая группа.", "Моя самая любимая песни группы Radiohead это Creep")
with open (filename, "w", encoding="utf-8") as file:
    for item in text:
      txt = file.write(item)
