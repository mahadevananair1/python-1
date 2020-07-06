f = open('from.txt')
for line in f:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

print('\n')

# Skipping with continue
f = open('from.txt')
for line in f:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)
