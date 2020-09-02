board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Global values
current_player = "X"

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

def handle_turn():
    display_board()

    while True:
        print(current_player + "'s turn")
        position = input("Choose a position from 1-9: ")

        valid = False
        while not valid:

            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Invalid input, Choose a position from 1-9: ")

            position = int(position) - 1
            if board[position] == "-":
                valid = True
            else:
                print("You can't go there, Go again")

    board[position] = current_player
    display_board()

handle_turn()
