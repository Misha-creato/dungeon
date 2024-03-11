import random


class Monster:
    def __init__(self, name: str, victory_chance: tuple):
        self.name = name
        self.gained_exp = self.get_gained_exp()
        self.victory_chance = self.get_victory_chance(victory_chance=victory_chance)

    def get_gained_exp(self):
        return random.randint(a=10, b=50)

    def get_victory_chance(self, victory_chance):
        a, b = victory_chance
        return random.randint(a=a, b=b)

    def __str__(self):
        return (f'Name: {self.name} | '
                f'Gained exp: {self.gained_exp} | '
                f'Victory chance: {self.victory_chance}'
                )
