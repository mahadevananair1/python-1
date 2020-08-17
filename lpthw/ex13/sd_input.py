from sys import argv

script, name, age, gender = argv

height = input("What is your height? ")
weight = input("What is your weight? ")

print(f"Your name is {name}")
print(f"You're {age} year old")
print(f"You're {gender}")
print(f"You're {height} tall")
print(f"You're weight {weight}")
