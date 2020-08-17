def elon_room():
    print("You found Elon!")
    print("You can ask Elon to give you money")

    choice = input("> ")

    how_much = int(choice)

    if how_much < 1000:
        print(f"Elon gave to ${how_much}, Enjoy!")
        exit(0)
    else:
        bad_luck("You greedy bastard!")


def tesla():
    print("You're in Tesla company")
    print("In here you may find Elon")
    print("We have door #1 and #2 for you")

    meet_elon = False
    while True:
        choice = input("> ")

        if choice == "1" and not meet_elon:
            bad_luck("You fall out of the building")
        elif choice == "2" and not meet_elon:
            print("Yay!, you meet Elon assistant")
            meet_elon = True
        elif choice == "meet elon" and meet_elon:
            elon_room()


def spacex():
    print("You're in Spacex company")
    print("You may and may not find Elon")
    print("We have door #1 and #2 for you")

    while True:
        choice = input("> ")

        if choice == "1":
            elon_room()
        elif choice == "2":
            bad_luck("Your open a exit door in spacex")
        else:
            print("I don't know, type a number 1 or 2")


def bad_luck(why):
    print(why, "try again next time")
    exit(0)


def start():
    print("We got two doors for you")
    print("We wanted you to choose anyone and play the game")
    print("If you're luckly, you can meet Elon Musk")
    print("Choose right or left?")

    while True:
        choice = input("> ")

        if choice == "right":
            tesla()
            break
        elif choice == "left":
            spacex()
            break
        else:
            print("I don't know what you want")


start()
