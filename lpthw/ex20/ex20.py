# import module
from sys import argv

# set up script and set a variable to argv
script, input_file = argv

# define a function and pass f as a argument
def print_all(f):
    # print argument with a read method
    print(f.read())

# define a function and pass f as a argument
def rewind(f):
    # set argument f with a method seek(0), seek(0) set the file's current position at the offset
    f.seek(0)

# define a function and pass line_count, f as a argument
def print_a_line(line_count, f):
    # print out line_count and f.readline()
    print(line_count, f.readline())

# set a variable for opening a file because if I pass input_file straight it will be a string
# and string doesn't have .read attribute on the object
# but open function has .read attribute on the object
current_file = open(input_file)

# print out a string
print("First let's print the whole file:\n")

# call a function and pass current_file
print_all(current_file)

# print out a string
print("Now let's rewind, kind of like a tape.")

# call a function and pass current_file
rewind(current_file)

# print out a string
print("Let's print three lines:\n")

# set a variable = 1
current_line = 1
# call a function and pass argument
print_a_line(current_line, current_file)

# set a new variable and get the old variable and + 1 to it, and stored to new variable
current_line = current_line + 1
# call a function and pass argument with new variable
print_a_line(current_line, current_file)

# set a new variable and get the old variable and + 1 to it, and stored to new variable
current_line = current_line + 1
# call a function and pass argument with new variable
print_a_line(current_line, current_file)

