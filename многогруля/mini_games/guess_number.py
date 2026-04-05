import random
from game_logic import GameState # имопрт библиотек и из гейм логики калсса геймстайт

def play(players):
    game_state = GameState(players)
    secret_number = random.randint(1, 100) # туту собственно обычная игра и ничего мне кажется обьяснять не надо
    max_attempts = 7
    print(f"\nИгра «Угадай число»: угадайте число от 1 до 100 за {max_attempts} попыток.")
    for attempt in range(max_attempts):
        for player in players:
            try:
                guess = int(input(f"{player}, ваша попытка {attempt + 1}: "))
            except ValueError:
                print("Введите целое число!")
                continue
            if guess == secret_number:
                game_state.update_score(player, 1)
                print(f"Поздравляем, {player}! Вы угадали число {secret_number}!")
                return
            elif guess < secret_number:
                print("Слишком мало!")
            else:
                print("Слишком много!")
    print(f"Никто не угадал! Загаданное число: {secret_number}")
