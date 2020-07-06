fname = input('Enter a file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    count += 1

print('There were', count, 'lines in', fname)
