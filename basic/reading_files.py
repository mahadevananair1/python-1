name = open("name.txt", "r")
for names in name.readlines():
    print(names)
name.close()
