board = [[1, 1, 1], [0, 2, 2], [2, 2, 0]]


def check(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            print("X won")


if check(1):
    won = True
if check(2):
    won = True
