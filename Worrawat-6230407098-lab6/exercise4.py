with open("kku2.txt", "w", encoding="utf8") as file2:
    with open("kku.txt", "r", encoding="utf8") as writing:
        word = writing.read()
        writing.close()
    file2.write(word)
    file2.write("\nMotto: วิทยา จริยา ปัญญา\nMotto in English: Knowledge, Virtues, Wisdom")
    file2.close()
with open("kku2.txt", "r", encoding="utf8") as fileread:
    read = fileread.read()
    print(read)
    fileread.close()
