board = [[1, 2, 0], [1, 1, 1], [1, 2, 0]]

# 4:08:00 strager explain def for me

# def check(num):
#     for row in board:
#         print(row)
#         for tile in row:
#             if tile == num:
#                 continue
#             else:
#                 break
#         else:
#             print("X won")

#     for column in range(3):
#         for row in board:
#             if row[column] == num:
#                 continue
#             else:
#                 break
#         else:
#             print("X won")
#
# if check(1):
#     won = True
# if check(2):
#     won = True

# for column in range(3):
#     print('\n')
#     for row in board:
#         print(row[column])

# for column in range(3):
#     for row in board:
#         print(row)
#         print(row[column])

# column = 2
# for row in board:
#     print(row)
#     print(row[column])

board_first = [1, 2, 0]
board_second = [1, 1, 1]
board_third = [1, 2, 0]
board = [board_first, board_second, board_third]
for column in range(3):
    for row in board:
        print(row)

        print(row[column])

# column = 0
# for row in board:
#     print(row)
#     print(row[column])

# just check the game state on every move, once it ends(shows winner), then you can reset it?