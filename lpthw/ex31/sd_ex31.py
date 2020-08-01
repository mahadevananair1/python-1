import time

user = input("""You have to two door
Choose anyone #1 and #2?
:""")

if user == '1':
    print("You enter Elon Musk room")
    print("You should be proud at you made right decision")
    print("He will give a advice to you")

    decision = input("Do you want or no [Y/n] ")

    if decision == 'Y':
        print("Take Risk, Work Hard, Do The Thing That Interest You And You Enjoy")
    elif decision == 'n':
        print("No advice for you because you choose [n]")
    else:
        print("You choose nothing either choose [Y/n]")

elif user == '2':
    print("You jump of a building")
    time.sleep(1)
    print("You fall")
    time.sleep(2)
    print("You're die")
