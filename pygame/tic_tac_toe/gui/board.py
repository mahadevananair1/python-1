board = [[1, 0, 2], [1, 1, 2], [1, 2, 0]]

def check(num):
    for column in range(3):
        for row in board:
            print(row[column] == num)

if check(1):
    print("x won")
if check(2):
    print("O won")
