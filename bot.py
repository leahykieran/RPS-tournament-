from enum import Enum
from random import randint


class Bot:
    def __init__(self, name):
        self.name = "BOT"
        self.score = 0
        self.choice = None

    def next_move(self):
        return RPS(randint(1, 3))



class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        return self.name