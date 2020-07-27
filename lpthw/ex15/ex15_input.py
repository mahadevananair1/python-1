print("Enter your filename:")
filename = input("> ")

txt = open(filename)
print(txt.read())
txt.close()
