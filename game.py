from player import Player
from monster import Monster
import os
import json
import random


MONSTER_FILE = 'monsters.json'


class Game:
    def __init__(self, player: Player):
        self.player = player
        self.all_monsters = []

    def start_game(self):
        self.set_all_monsters()
        while self.player.is_alive:
            self.player_move()

    def get_monsters_file(self):
        if os.path.isfile(MONSTER_FILE) and os.path.getsize(MONSTER_FILE) > 0:
            print(f"File {MONSTER_FILE} found")
        else:
            print(f"File {MONSTER_FILE} damaged or doesn't exist")
            print('Please wait...')
    #         download file

    def set_all_monsters(self):
        with open(MONSTER_FILE, 'r') as f:
            data = json.load(f)
        for v in data.values():
            names = [name['name'] for name in v]
            self.all_monsters.extend(names)
        random.shuffle(self.all_monsters)

    def get_monster(self):
        monster = Monster(
            name=self.all_monsters[0],
            victory_chance=(self.player.victory_chance_min, self.player.victory_chance_max)
        )
        return monster

    def player_move(self):
        print(self.get_monster())
        print('Your statistics:')
        print(self.player)


game = Game(player=Player())
game.start_game()
