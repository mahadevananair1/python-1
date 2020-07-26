name = 'Jan Poonthong'
age = 16 # not a lie
height = 70 # inches
weight = 150 # lbs
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the tea.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# convert
inches = 80
pounds = 160

centimeters = inches * 2.54
kilogram = pounds * 0.4535924
print(f"This is 80 inches to centimeters {round(centimeters)}.")
print(f"This is 160 pounds to kilogram {round(kilogram)}.")

