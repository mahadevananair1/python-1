# define a function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print out a f-string inside a functions and use arguments
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print out a string
print("We can just give the function number directly:")
# call the function and give it a arguments
cheese_and_crackers(20, 30)

# print out a string
print("Or, we can use variable from our script:")
# make a variables
amount_of_cheese = 10
amount_of_crackers = 50

# call the function and give it a argument of variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print out a string
print("We can even do math inside too:")
# call the function and do math inside
cheese_and_crackers(10 + 20, 5 + 6)

# print out a string
print("And we can combine the two, variable and math:")
# call the function and do math inside with a variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
