import random
import time
import os
from game_logic import GameState
COLORS = ['красный', 'синий', 'зелёный', 'жёлтый', 'оранжевый', 'фиолетовый'] #цвета для запоминания

def clear_screen():
    #очистка экрана
    os.system('cls' if os.name == 'nt' else 'clear')
def play(players):
    game_state = GameState(players)
    print("\nИгра «Память на цвета»: запомните последовательность!")
    #создаем последовательность из 4 цветов()
    sequence = [random.choice(COLORS) for _ in range(4)]
    print("Запоминайте:")
    # показываем каждый цвет с задержкой, затем очищаем экран
    for color in sequence:
        print(color)
        time.sleep(2)  # даём больше времени на запоминание (2 секунды)
        clear_screen()  # очищаем экран после показа каждого цвета
    # после показа всех цветов небольшой перерыв перед вводом
    print("Теперь повторите последовательность!")
    time.sleep(1)
    for player in players:
        print(f"\n{player}, введите последовательность цветов:")
        correct = True
        # собираем ввод игрока
        player_input = []
        for i in range(4):
            while True:
                guess = input(f"Цвет {i+1}: ").lower().strip()
                if guess in COLORS:
                    player_input.append(guess)
                    break
                else:
                    print(f"Неверный цвет! Доступные: {', '.join(COLORS)}")
        # проверяем всю последовательность после ввода
        if player_input == sequence:
            game_state.update_score(player, 1)
            print("Отлично! Вы запомнили всю последовательность!")
        else:
            print(f"Неверно! Правильный порядок: {', '.join(sequence)}")
            print("Попробуйте ещё раз!")
    winner = game_state.get_winner()
    print(f"\nПобедитель: {winner}!")
