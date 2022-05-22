file1 = open('wordsalt.txt', 'r', encoding="ANSI")
file2 = open('words5.txt', 'w')
Lines = file1.readlines()
words = []
for line in Lines:
    if len(line.strip()) == 5:
        file2.write(line.strip() + "\n")
