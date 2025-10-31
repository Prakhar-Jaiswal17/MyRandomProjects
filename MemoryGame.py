import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board, revealed):
    clear_screen()
    print("Memory Game\n")
    for row in range(4):
        for col in range(4):
            if revealed[row][col]:
                print(f"{board[row][col]:^4}", end=" ")
            else:
                print(" * ", end=" ")
        print()

def check_win(revealed):
    return all(all(row) for row in revealed)

def create_board():
    symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 2
    random.shuffle(symbols)
    board = [symbols[i:i + 4] for i in range(0, 16, 4)]
    return board

def memory_game():
    board = create_board()
    revealed = [[False] * 4 for _ in range(4)]
    attempts = 0

    print("Welcome to Memory Game!")
    time.sleep(1)

    while True:
        display_board(board, revealed)

        print("\nChoose the first card (row col): ")
        row1, col1 = map(int, input("Enter row and column (0-3) separated by space: ").split())
        if revealed[row1][col1]:
            print("Card already revealed! Try again.")
            time.sleep(1)
            continue
        
        revealed[row1][col1] = True
        display_board(board, revealed)

        print("\nChoose the second card (row col): ")
        row2, col2 = map(int, input("Enter row and column (0-3) separated by space: ").split())
        if revealed[row2][col2]:
            print("Card already revealed! Try again.")
            time.sleep(1)
            revealed[row1][col1] = False
            continue

        revealed[row2][col2] = True
        display_board(board, revealed)

        attempts += 1
        if board[row1][col1] != board[row2][col2]:
            print("\nNo match! Cards will be hidden again.")
            time.sleep(1)
            revealed[row1][col1] = False
            revealed[row2][col2] = False
        else:
            print("\nIt's a match! Well done.")
            time.sleep(1)

        if check_win(revealed):
            display_board(board, revealed)
            print(f"\nCongratulations! You matched all pairs in {attempts} attempts!")
            break

if __name__ == "__main__":
    memory_game()
