formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Out of the night that covers me",
    "Black as the pit from pole to pole",
    "I thank whatever gods may be",
    "For my unconquerable soul."
))
