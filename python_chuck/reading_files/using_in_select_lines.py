f = open('from.txt')
for line in f:
    line = line.rstrip()
    if not '@gmail.com' in line:
        continue
    print(line)
