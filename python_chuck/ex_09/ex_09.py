fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'clown.txt'
fhand = open(fname)

di = dict()
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w, 0) + 1

# now we want to find the most common word
largest = -1
word = None
for key, value in di.items():
    if value > largest:
        largest = value
        word = key # cature/remember the word that was largest

print(word, largest)
