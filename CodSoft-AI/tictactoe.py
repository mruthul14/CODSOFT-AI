import random

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])

def check_win(player):
    win_conditions = [(0,1,2),(3,4,5),(6,7,8),
                      (0,3,6),(1,4,7),(2,5,8),
                      (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_conditions)

def player_move():
    move = int(input("Enter position (0-8): "))
    if board[move] == " ":
        board[move] = "X"

def ai_move():
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"

for _ in range(9):
    print_board()
    player_move()
    if check_win("X"):
        print("You win!")
        break

    ai_move()
    if check_win("O"):
        print("AI wins!")
        break