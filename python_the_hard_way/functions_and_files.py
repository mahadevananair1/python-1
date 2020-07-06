from sys import argv

# Create a script
script, input_file = argv

# Creating a functions
def print_all(f):
    print(f.read())

def rewind(f):
    # 0: means your reference point is the beginning of the file
    f.seek(0)

# Creating line_count
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open input_file
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# Line = 1
current_line = 1
print_a_line(current_line, current_file)

# Line = 2
current_line += 1
print_a_line(current_line, current_file)

# Line = 3
current_line += 1
print_a_line(current_line, current_file)
