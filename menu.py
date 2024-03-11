from game import Game
from player import Player
import os
import json


SAVE_FILE = 'save.json'


class Menu:
    def greeting(self):
        print('Hello!')

    def game_settings(self):
        player = self.get_player()
        game = Game(player=player)
        game.start_game()


    def get_saved_player(self):
        if os.path.isfile(SAVE_FILE) and os.path.getsize(SAVE_FILE) > 0:
            with open(SAVE_FILE, 'r') as f:
                data = json.load(f)
            return Player(**data)
        else:
            print(f"File {SAVE_FILE} damaged or doesn't exist")
            return None

    def get_player(self):
        player = None
        while player is None:
            answer = self.get_user_answer()
            if answer == '1':
                player = Player()
            elif answer == '2':
                player = self.get_saved_player()
            else:
                pass
        return player

    def get_user_answer(self):
        while True:
            answer = input('Select: 1.Start new game 2.Continue game 3.Exit: ')
            if answer in ['1', '2', '3']:
                return answer
