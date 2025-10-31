board = [[" "] * 3 for _ in range(3)]
players = ["X", "O"]
turn = 0

while True:
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")
    
    player = players[turn % 2]
    move = input(f"Player {player}, enter your move (row col): ")
    row, col = map(int, move.split())
    
    if board[row][col] == " ":
        board[row][col] = player
    else:
        print("This spot is already taken. Try again.")
        continue

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player or board[0][i] == board[1][i] == board[2][i] == player:
            print(f"Player {player} wins!")
            exit()
    
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        print(f"Player {player} wins!")
        exit()

    if all(cell != " " for row in board for cell in row):
        print("It's a draw!")
        exit()

    turn += 1
