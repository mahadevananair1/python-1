# This program has white space in it, so to fixed I made a new file name searching_file_fixed.py
f = open('from.txt')
for line in f:
    if line.startswith('From:'):
        print(line)
