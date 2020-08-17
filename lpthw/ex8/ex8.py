# create a variable and assign to a string
formatter = "{} {} {} {}"

# print it out and formated to variable = formatter and pass in four arguments, which match up with the four {} in the formatter variable
# the result of calling format on formatter is new string
print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
