
import os
import json
from game import Game
from player import Player



class Interface:
    def greeting(self):
        print('Hello!')

    def game_settings(self):
        player = self.get_player()
        game = Game(player=player)

        game.start_game()
        while game.player.is_alive:
            game.get_monster()
            self.print_player_move(game=game)
            answer = self.get_user_answer(text='1.Fight 2.Run 3.Exit game: ')

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
            answer = self.get_user_answer(text='Select: 1.Start new game 2.Continue game 3.Exit: ')
            if answer == '1':
                player = Player()
            elif answer == '2':
                player = self.get_saved_player()
            else:
                pass
        return player

    def get_user_answer(self, text: str):
        while True:
            answer = input(text)
            if answer in ['1', '2', '3']:
                return answer

    def print_player_move(self, game: Game):
        print(game.current_monster)
        print('Your statistics:')
        print(game.player)

