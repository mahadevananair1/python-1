# import modules
from sys import argv

# set a variable to argv
script, filename = argv

# open filename
txt = open(filename)

# print out a string and filename
print(f"Here's your file {filename}:")
# print out all inside a file
print(txt.read())
