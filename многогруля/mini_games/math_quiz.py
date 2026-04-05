import random
from game_logic import GameState
import time #база всех игр
def play(players):
    game_state = GameState(players)
    print("\nИгра «Математический тест»: решите 5 примеров за 30 секунд!")
    for player in players:
        print(f"\nХод {player}:")
        score = 0
        start_time = time.time()# вывод рандомного чтсла в пределах 20 и еще одного такого же и рандомнй операции с учетом правильного ответа на пример
        for _ in range(5):
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            op = random.choice(['+', '-', '*'])
            if op == '+':
                correct = a + b
            elif op == '-':
                correct = a - b
            else:
                correct = a * b
            print(f"{a} {op} {b} = ?")
            try:
                answer = int(input("Ваш ответ: "))
                if answer == correct:
                    score += 1
                    print("Правильно!") #если ответ правильный
                else:
                    print(f"Неверно! Правильный ответ: {correct}") # неправильный
            except ValueError:
                print("Введите целое число!")
        end_time = time.time()
        elapsed = end_time - start_time
        if elapsed <= 30:
            game_state.update_score(player, score)
            print(f"{player} набрал {score} очков!") # подсчет очков
        else:
            print(f"{player} превысил лимит времени! Очки не начисляются.")#для хитрецов)))
    winner = game_state.get_winner()
    print(f"\nПобедитель: {winner}!")
