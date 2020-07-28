from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(2)

# set a variable for opening a file because if I pass input_file straight it will be a string
# and string doesn't have .read attribute on the object
# but open function has .read attribute on the object
current_file = open(input_file)

def print_a_line(line_count, f):
    print(line_count, f.readline())

print_all(current_file)
rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# or

#for i in range(3):
    #i = i + 1
    #print_a_line(i, current_file)
