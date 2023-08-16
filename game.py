def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for line in board + list(zip(*board)) + [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]:
        if all(cell == player for cell in line):
            return True
    return False


def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Игрок {players[current_player]}, выберите строку (0-2): "))
        col = int(input(f"Игрок {players[current_player]}, выберите столбец (0-2): "))

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Игрок {players[current_player]} победил!")
                break
            elif is_full(board):
                print_board(board)
                print("Ничья!")
                break
            current_player = 1 - current_player
        else:
            print("Эта клетка уже занята. Попробуйте снова.")


if __name__ == "__main__":
    tic_tac_toe()
