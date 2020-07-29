import math
def multiply(a, b):
    print(f"Income: {a}, Hours: {b}")
    return a * b

def after_five_year(age):
    return age + 5

def add(a, b):
    return a + b

def subtract(a, b):
    return a -b
# the function has been called and pass in a argument and print it all out
# return on the function is also printed (answer)
print(multiply(50, 5))

# the function has been called and pass in a argument
# return on the function will not been shown 
multiply(50, 5)  

# the function has been called and pass in a argument and print it all out
# return on the function is also printed (answer)
print(after_five_year(16))

# work from backward and calculate
print(subtract(200, add(40, multiply(60, 2))))

