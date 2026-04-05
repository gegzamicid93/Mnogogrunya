from game_logic import GameState
import random

def play(players):
    game_state = GameState(players)
    choices = {'к': 'камень', 'н': 'ножницы', 'б': 'бумага'} #выбираем скоращенноую вещь для игры
    print("\nИгра «Камень‑ножницы‑бумага»")
    print("Используйте: к — камень, н — ножницы, б — бумага")
    for round_num in range(3):  # 3 раунда
        print(f"\nРаунд {round_num + 1}:")
        player_choices = {}
        for player in players:
            while True:
                choice = input(f"{player}, ваш выбор (к/н/б): ").lower()
                if choice in choices:
                    player_choices[player] = choice
                    break
                else:
                    print("Неверный ввод! Используйте к, н или б.") # проверк на валидность
        # определяем побидителя в раунде
        unique_choices = set(player_choices.values())
        if len(unique_choices) == 1:
            print("Ничья в раунде!")
        else:
            # простая логика для 2 игроков
            p1, p2 = players[0], players[1]
            c1, c2 = player_choices[p1], player_choices[p2]
            if (c1 == 'к' and c2 == 'н') or (c1 == 'н' and c2 == 'б') or (c1 == 'б' and c2 == 'к'):
                game_state.update_score(p1, 1)
                print(f"{p1} выиграл раунд!")
            elif (c2 == 'к' and c1 == 'н') or (c2 == 'н' and c1 == 'б') or (c2 == 'б' and c1 == 'к'):
                game_state.update_score(p2, 1)
                print(f"{p2} выиграл раунд!")
            else:
                print("Ничья в раунде!") # ну а тут тупо условия игры как в реал лайф
    winner = game_state.get_winner()
    print(f"\nОбщий победитель: {winner}!")
