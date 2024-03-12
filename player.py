import json
from dataclasses import dataclass, field
from constants import SAVE_FILE
from monster import Monster


@dataclass
class Player:

    level: int = 1
    experience: int = 0
    level_up_experience: int = 100
    energy: int = 100
    level_energy: int = 100
    victory_chance_min: int = 50
    victory_chance_max: int = 90
    defeated_monsters: list = field(default_factory=list)
    is_alive: bool = True

    def load_player_data(self):
        with open(SAVE_FILE, 'r') as file:
            data = json.load(file)
        self.level = data['level']
        self.experience = data['experience']
        self.level_up_experience = data['level_up_experience']
        self.energy = data['energy']
        self.level_energy = data['level_energy']
        self.victory_chance_min = data['victory_chance_min']
        self.victory_chance_max = data['victory_chance_max']
        self.defeated_monsters = data['defeated_monsters']

    def decrease_energy(self, energy_points: int):
        self.energy -= abs(energy_points)
        if self.energy <= 0:
            self.is_alive = False

    def increase_experience(self, experience_points: int):
        self.experience += experience_points
        exp_diff = self.level_up_experience - self.experience
        if exp_diff <= 0:
            self.update_stats(exp_diff)

    def update_stats(self, add_experience_points: int):
        self.level += 1
        self.level_energy += 10
        self.energy = self.level_energy
        self.experience = 0
        self.experience += abs(add_experience_points)
        self.level_up_experience = int(self.level_up_experience * 1.5)
        self.victory_chance_min -= 1
        self.victory_chance_max -= 1

    def update_monsters_list(self, defeated_monster: Monster):
        if self.defeated_monsters is None:
            self.defeated_monsters = []
        self.defeated_monsters.append(defeated_monster)

