# Creating Function
def cheese_and_crackers(chese_count, boxes_of_crackers):
    print(f"You have {chese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")
# Passing a numbers
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
# Creating variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
# Passing new argument to function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# Math in argument
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# Combine math and variables
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
