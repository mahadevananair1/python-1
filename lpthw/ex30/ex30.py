people = 30
cars = 20
trucks = 15

# check if is True or False
if cars > people or trucks < cars:
    print("We should take the cars")
# if False goes to elif
elif cars < people:
    print("We should not take the cars")
# elif False goes to else and print
else:
    print("We can't decide")

if trucks > cars:
    print("That's too mant trucks")
elif trucks < cars:
    print("Maybe we could take the trucks")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks")
else:
    print("Fine, let's stay home then")
