from sys import argv 

script, file_name = argv

in_file = open(file_name)
in_data = in_file.readlines()

num = len(in_data)

n = 0
for elem in in_data:
    n += 1
    print(n, elem)

for i, l in enumerate(in_data):
    print(i, l)

in_file.close()
