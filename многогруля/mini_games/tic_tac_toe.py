from game_logic import GameState
def print_board(board):
    for row in board:
        print(' | '.join(row))
        if row != board[-1]:
            print("---------")
def check_winner(board, player):
    # проверка строк, столбцов и диагоналей
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
# прорисовка поля сверху а с нмху фигуры хотьбы и смысл игрового процесса
def play(players):
    game_state = GameState(players)
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player_idx = 0
    symbols = ['X', 'O']
    print("\nИгра «Крестики‑нолики»")
    for move in range(9):
        current_player = players[current_player_idx]
        symbol = symbols[current_player_idx %2]
        print_board(board)
        print(f"\nХод {current_player} ({symbol}):")
        while True:
            try:
                row = int(input("Строка (0–2): "))
                col = int(input("Столбец (0–2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                    board[row][col] = symbol
                    break
                else:
                    print("Неверная позиция! Попробуйте снова.")
            except ValueError:
                print("Введите числа 0–2.")

        if check_winner(board, symbol):
            game_state.update_score(current_player, 1)
            print(f"\n{current_player} выиграл!")
            print_board(board)
            return
        current_player_idx += 1
    print("\nНичья!")
    print_board(board)
