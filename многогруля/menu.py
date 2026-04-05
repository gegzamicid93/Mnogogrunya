from mini_games.guess_number import play as play_guess_number
from mini_games.bulls_and_cows import play as play_bulls_and_cows
from mini_games.math_quiz import play as play_math_quiz
from mini_games.word_guessing import play as play_word_guessing
from mini_games.rock_paper_scissors import play as play_rock_paper_scissors
from mini_games.tic_tac_toe import play as play_tic_tac_toe
from mini_games.number_sequence import play as play_number_sequence
from mini_games.color_memory import play as play_color_memory
#вызываем игры, то есть полключаем функцию play из каждого модуля мини- игр
def main_menu():
    print("===МНОГОГРУНЯ===")
    # выбор количества игроков
    while True:
        try:
            players_count = int(input("Введите количество игроков (2 или 4): ")) # поставлен пробел для выбора
            if players_count in [2, 4]:
                break
            else:
                print("Ошибка! Введите 2 или 4") # проверочка на правильный вввод
        except ValueError:
            print("Ошибка! Введите число.") 
    players = [f"Игрок {i+1}" for i in range(players_count)] 
    #меню выбора игры
    print("\nВыберите игру:")
    print("1. Угадай число")
    print("2. Быки и коровы")
    print("3. Математический тест")
    print("4. Угадай слово")
    print("5. Камень‑ножницы‑бумага")
    print("6. Крестики‑нолики")
    print("7. Числовая последовательность")
    print("8. Память на цвета") 
    while True:
        choice = int(input("Ваш выбор (1–8): ")) # выбор игры, если один то запуск одной игры если 2 то творой и  тд и тп
        if choice == 1:
            play_guess_number(players)
            break
        elif choice == 2:
            play_bulls_and_cows(players)
            break
        elif choice == 3:
            play_math_quiz(players)
            break
        elif choice == 4:
            play_word_guessing(players)
            break
        elif choice == 5:
            play_rock_paper_scissors(players)
            break
        elif choice == 6:
            play_tic_tac_toe(players)
            break
        elif choice == 7:
            play_number_sequence(players)
            break
        elif choice == 8:
            play_color_memory(players)
            break
        else:
            print("Ошибка! Выберите от 1 до 8") # снова проверка на валидонсть
