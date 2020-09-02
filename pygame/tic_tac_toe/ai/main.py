board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Global values
game_still_going = True
current_player = "X"

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

def handle_turn(player):
    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input, Choose a position from 1-9: ")

        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You can't go here, Go again")

    board[position] = player
    display_board()

def check_if_game_over():
    pass

def flip_player():
    pass

play_game()
