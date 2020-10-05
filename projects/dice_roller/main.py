from random import randint

repeat = True
while repeat:
    print('You rolled', randint(1, 6))
    x = input('Do you want to roll again? Y/N: ').lower()
    if x == 'y' or x == 'yes':
        repeat = True
    else:
        repeat = False
