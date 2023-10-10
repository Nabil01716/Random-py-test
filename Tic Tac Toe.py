import random

def print_board(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    while True:
        print_board(board)
        if current_player == "X":
            row, col = map(int, input("Enter your move (row[1-3] column[1-3]): ").split())
            row -= 1
            col -= 1
        else:
            row, col = computer_move(board)

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(current_player + " wins! Congratulations!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw! Good game!")
                break
            else:
                current_player = "X" if current_player == "O" else "O"
        else:
            print("Invalid move. Try again.")

play_tic_tac_toe()
#now play this shit..