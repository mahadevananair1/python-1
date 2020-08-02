from sys import argv 

script, file_name = argv

in_file = open(file_name)
in_data = in_file.readlines()

num = len(in_data)

for line in in_data:
    print(line)

for count in range(1, num + 1):
    print(count)

in_file.close()
