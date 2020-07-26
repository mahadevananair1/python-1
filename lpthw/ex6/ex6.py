# variable set to 10
types_of_people = 10
# f-string the variable = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# f-string the variable
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# f-string the variable and print it out
print(f"I said: {x}")
print(f"I also said:'{y}'")

hilarious = False
# f-string without variable 
joke_evaluation = "Isn't that joke so funny?! {}"

# print out the variable and format(hilarious) to the variable name joke_evaluation
print(joke_evaluation.format(hilarious))

# set string in a variables
w = "This is the left side of..."
e = "a string with a right side."

# print them out and joining them (no space because is +)
# if it comman(,), there will be space
print(w + e)
