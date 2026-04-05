# импортируем тип List из модуля typing это нужно для указания типов 
from typing import List

# определяем класс GameState, который будет хранить состояние текущей игры
class GameState:
    # конструктор класса вызывается при создании нового объекта GameState
    def __init__(self, players: List[str], max_rounds: int = 3):
        # сохраняем список игроков 
        self.players = players
        # сохраняем максимальное количество раундов
        self.max_rounds = max_rounds
        # создаём словарь для хранения очков: каждому игроку изначально присваиваем 0 очков
        self.scores = {player: 0 for player in players}

    #для обновления счёта конкретного игрока
    def update_score(self, player: str, points: int):
        # увеличиваем счёт игрока на указанное количество очков
        # если игрок уже есть в словаре, его счёт обновляется
        self.scores[player] += points
    # метод для определения победителя игры
    def get_winner(self) -> str:
        # используем функцию max() с параметром key, чтобы найти имя игрока
        return max(self.scores, key=self.scores.get)
