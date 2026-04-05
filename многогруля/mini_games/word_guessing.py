import random # бибелотека для ранломных слов
from game_logic import GameState

WORDS = ['программирование', 'компьютер', 'алгоритм', 'переменная', 'функция'] #слова для запоминания
def play(players):
    game_state = GameState(players)
    secret_word = random.choice(WORDS)
    guessed = ['_'] * len(secret_word)
    attempts = 10
    print(f"\nИгра «Угадай слово»: угадайте слово из {len(secret_word)} букв за {attempts} попыток.")
    print(' '.join(guessed))
# ниже игровой процесс тупоооо
    while attempts > 0 and '_' in guessed:
        for player in players:
            print(f"\n{player}, ваша попытка ({attempts} осталось):")
            guess = input("Введите букву или слово целиком: ").lower()
            if len(guess) == 1:
                if guess in secret_word:
                    for i, letter in enumerate(secret_word):
                        if letter == guess:
                            guessed[i] = guess
                    print("Есть такая буква!")
                else:
                    print("Такой буквы нет!")
                    attempts -= 1
            else:
                if guess == secret_word:
                    guessed = list(secret_word)
                    break
                else:
                    print("Неверное слово!")
                    attempts -= 1
            print(' '.join(guessed))
            if '_' not in guessed:
                break
    if '_' not in guessed:
        game_state.update_score(players[0], 1)  # очко получает первый угадавший
        print(f"Поздравляем! Слово '{secret_word}' угадано!")
    else:
        print(f"Никто не угадал! Загаданное слово: '{secret_word}'")
