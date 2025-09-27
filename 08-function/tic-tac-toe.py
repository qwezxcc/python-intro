import json
import os

# 0.0 0.1 0.1
# 1.0 1.1 1.2
# 2.0 2.2 2.2

FILENAME = 'board.json'
board = {}

if os.path.exists(FILENAME):
    with open(FILENAME, 'r', encoding="utf-8") as f:
        board = json.load(f)


board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
         ]

current_player = 1
winner = None
move_count = 0

def print_board():
    print('\nПоточний статус: ')
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | ")
    print('-' * 13)
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | ")
    print('-' * 13)
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | ")
    print()

while True:
    row, col = None, None
    print_board()

    valid_mode = False
    while not valid_mode:
        move_input = input(f'Гравець {current_player} ходить: ')

        # 2.0, 0.0

        parts = move_input.split(".")
        row = int(parts[0])
        col = int(parts[1])

        # check
        if row < 0 or row > 2 or col < 0 or col > 2:
            print('Неправильна позиція')
            continue

        if board[row][col] != ' ':
            print("Клітинка зайнята!")
            continue

        valid_mode = True

        move_count += 1

    if current_player == 1:
        board[row][col] = 'x'
    else:
        board[row][col] = 'o'

    # checking all rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            winner = current_player
            break

    # checking all columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            winner = current_player
            break

    if winner is not None:
        break

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        winner = current_player
        break

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        winner = current_player
        break

    if move_count >= 9 and winner is None:
        winner = 0
        break

    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

print_board()

print('=' * 20)
if winner:
    print(f"Гравець {current_player} переміг")
else:
    print("Нічия!")



with open(FILENAME, 'w', encoding="utf-8") as f:
    json.dump(board, f, ensure_ascii=False, indent=4)
