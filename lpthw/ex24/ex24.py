print("Let's practice everything.")
print('You\'d need to know \'bount escapes with \\ that do:')
print('\n newline and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanantion
\n\twhere there is none.
"""
print("-------------------")
print(poem)
print("-------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
# create three variable and assgined to called function which is pass with start_point
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))

print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
# create a variable and assgined to called function which is pass with start_point
# but inside function there is three variable, and you make it into one
formula = secret_formula(start_point)
# other way of formating a string, and you get all variable within a function, with a *
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
