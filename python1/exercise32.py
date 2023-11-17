board = [" " for _ in range(9)]
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])
def check_win(player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False
current_player = "X"
game_over = False
while not game_over:
    display_board()
    print(f"Player {current_player}'s turn. Enter position (1-9): ")
    try:
        position = int(input()) - 1
        if position < 0 or position > 8 or board[position] != " ":
            print("Invalid move. Try again.")
            continue
        board[position] = current_player
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif " " not in board:
            display_board()
            print("It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"
    except ValueError:
        print("Invalid input. Enter a number between 1 and 9.")
print("Game over. Thanks for playing!")