import random
from game_logic import GameState # делем тоже самое для всех игр собственно обьяснила это в первой игре самой
def generate_secret():
    digits = list(range(10))
    random.shuffle(digits) # в этих строчках сам смысл игры типо угадки числа (c 5 по 24)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits[:4]))

def count_bulls_and_cows(secret, guess):
    bulls = cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows
def play(players):
    game_state = GameState(players)
    secret = generate_secret()
    max_attempts = 10
    print(f"\nИгра «Быки и коровы»: угадайте 4-значное число за {max_attempts} попыток.")
    print("Бык — правильная цифра на правильной позиции.")
    print("Корова — правильная цифра, но на неправильной позиции.") # занкмоство с игрой
    for attempt in range(max_attempts):
        for player in players:
            guess = input(f"{player}, попытка {attempt + 1}: ") # начисление попыток
            if not (len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4):
                print("Введите 4 разные цифры!")
                continue
            bulls, cows = count_bulls_and_cows(secret, guess)
            print(f"Быки: {bulls}, Коровы: {cows}")
            if bulls == 4:
                game_state.update_score(player, 1)
                print(f"{player} выиграл! Число: {secret}") # когда отгадали и быков стало 4 то есть все верно
                return
    print(f"Никто не угадал! Число было: {secret}")
