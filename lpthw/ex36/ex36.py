from sys import argv 

script, file_name = argv

in_file = open(file_name)
in_data = in_file.readlines()

num = len(in_data)

n = 0
for elem in in_data:
    n += 1
    print(n, elem)

in_file.close()
