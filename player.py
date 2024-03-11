

class Player:
    def __init__(self,
                 level: int = 1,
                 experience: int = 0,
                 level_up_experience: int = 100,
                 energy: int = 100,
                 level_energy: int = 100,
                 level_experience: int = 100,
                 victory_chance_min: int = 50,
                 victory_chance_max: int = 90,
                 ):
        self.level = level
        self.experience = experience
        self.level_up_experience = level_up_experience
        self.energy = energy
        self.level_energy = level_energy
        self.level_experience = level_experience
        self.victory_chance_min = victory_chance_min
        self.victory_chance_max = victory_chance_max
        self.killed_monsters = []
        self.is_alive = True

    def update_energy(self, energy_points: int):
        self.energy += energy_points
        if self.energy <= 0:
            self.is_alive = False

    def update_experience(self, experience_points: int):
        self.level_up_experience -= experience_points
        if self.level_up_experience > 0:
            self.experience += experience_points
        else:
            self.update_stats()

    def update_stats(self):
        self.level += 1
        self.level_energy += 10
        self.energy = self.level_energy
        self.experience = 0
        self.experience += abs(self.level_up_experience)
        self.level_experience = int(self.level_experience * 1.5)
        self.level_up_experience = self.level_experience - abs(self.level_up_experience)
        self.victory_chance_min -= 1
        self.victory_chance_max -= 1

    def __str__(self):
        return (f'Level: {self.level} | Exp: {self.experience} |  '
                f'Level up experience: {self.level_up_experience} | '
                f'Energy: {self.energy} | Killed monsters: {self.killed_monsters}'
                )
