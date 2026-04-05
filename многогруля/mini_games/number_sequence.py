import random
from game_logic import GameState
def generate_sequence():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    return [start + i * step for i in range(5)] 
def play(players):
    game_state = GameState(players)
    print("\nИгра «Числовая последовательность»: продолжите последовательность!")
    for player in players:
        print(f"\nХод {player}:")
        sequence = generate_sequence()
        hidden_index = random.randint(2, 4)  # скрываем один из последних элементов
        display_sequence = sequence.copy()
        display_sequence[hidden_index] = '?'
        print("Продолжите последовательность:")
        print(' → '.join(map(str, display_sequence)))

        try:
            answer = int(input("Ваш ответ: "))
            if answer == sequence[hidden_index]:
                game_state.update_score(player, 1)
                print("Правильно!")
            else:
                print(f"Неверно! Правильный ответ: {sequence[hidden_index]}")
        except ValueError:
            print("Введите целое число!")

    winner = game_state.get_winner()
    print(f"\nПобедитель: {winner}!")
