import random
from constants import MIN_EXPERIENCE_POINTS, MAX_EXPERIENCE_POINTS


class Monster:
    def __init__(self, name: str, victory_chance_min: int, victory_chance_max: int):
        self.name = name
        self.gained_exp = self.get_gained_exp()
        self.victory_chance = self.get_victory_chance(
            victory_chance_min=victory_chance_min,
            victory_chance_max=victory_chance_max
        )

    def get_gained_exp(self):
        return random.randint(a=MIN_EXPERIENCE_POINTS, b=MAX_EXPERIENCE_POINTS)

    def get_victory_chance(self, victory_chance_min: int, victory_chance_max: int):
        return random.randint(a=victory_chance_min, b=victory_chance_max)

