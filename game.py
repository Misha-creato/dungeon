import os
import json
import random
import sys

from encoders import MonsterJSONEncoder
from player import Player
from monster import Monster
from interface import Interface
from constants import (
    MONSTER_FILE,
    SAVE_FILE,
    RUN_ENERGY_POINTS,
    FIGHT_ENERGY_POINTS,
)


class Game:

    all_monsters: list = []
    current_monster: Monster = None
    retry: bool = None

    def __init__(self, player: Player, interface: Interface):
        self.player = player
        self.interface = interface

    def start_game(self):
        self.set_all_monsters()
        self.player.level_up = False
        while self.player.is_alive:
            self.retry = False
            self.get_monster()
            self.interface.print_player_move(player=self.player, monster=self.current_monster)
            answer = self.interface.get_user_answer(options=self.interface.player_move_options)
            self.player_move(player_answer=answer)
            self.save_progress()
        self.interface.print_end_game(player=self.player)
        self.clear_progress()

    def set_all_monsters(self):
        with open(MONSTER_FILE, 'r') as file:
            data = json.load(file)

        for monsters_category in data.values():
            names = [monster['name'] for monster in monsters_category]
            self.all_monsters.extend(names)

        random.shuffle(self.all_monsters)

    def get_monster(self):
        victory_chance_min = self.player.victory_chance_min
        victory_chance_max = self.player.victory_chance_max

        self.current_monster = Monster(
            name=random.choice(self.all_monsters),
            victory_chance_min=victory_chance_min,
            victory_chance_max=victory_chance_max
        )

    def player_move(self, player_answer: str):

        if player_answer == '1':
            self.player.decrease_energy(energy_points=FIGHT_ENERGY_POINTS)
            self.player_fight()
            is_run = False
        elif player_answer == '2':
            self.player.decrease_energy(energy_points=RUN_ENERGY_POINTS)
            is_run = True
        else:
            self.interface.print_results(player=self.player)
            sys.exit(0)

        self.interface.player_move_result(
            retry=self.retry,
            is_run=is_run,
            monster=self.current_monster
        )

        if self.player.level_up:
            self.interface.print_level_up()
            self.player.level_up = False

        if self.retry and self.player.is_alive:
            self.try_again()

    def player_fight(self):
        victory_chance = self.current_monster.victory_chance / 100
        self.retry = True

        if random.random() < victory_chance:
            self.retry = False
            self.player.update_monsters_list(defeated_monster=self.current_monster)
            self.player.increase_experience(experience_points=self.current_monster.gained_exp)

    def try_again(self):
        answer = self.interface.get_user_answer(options=self.interface.player_try_options)

        if answer == '1':
            self.interface.print_player_move(player=self.player, monster=self.current_monster)
            self.player_move(player_answer='1')
        elif answer == '3':
            self.interface.print_results(player=self.player)
            sys.exit(0)

    def save_progress(self):
        player_stats = vars(self.player)
        with open(SAVE_FILE, "w") as outfile:
            json.dump(player_stats, outfile, cls=MonsterJSONEncoder, indent=2)

    def clear_progress(self):
        os.remove(SAVE_FILE)
