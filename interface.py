import time

from player import Player
from monster import Monster
from prettytable import PrettyTable


class Interface:

    player_menu_options = {'1': 'Start new game',
                           '2': 'Load save',
                           '3': 'Exit game',
                           }
    player_move_options = {'1': 'Fight monster',
                           '2': 'Run',
                           '3': 'Exit game',
                           }
    player_try_options = {'1': 'Fight monster again',
                          '2': 'Continue game',
                          '3': 'Exit game',
                          }

    def greeting(self):
        print('Hello! Welcome to Dungeon game!')
        print('Checking files...')
        time.sleep(1)

    def print_results(self, player: Player):
        print('Game will be closed.')
        print('Your results:')
        self.print_player(player=player)

    def print_end_game(self, player: Player):
        print('Oops, your energy ran out. That was a great game!')
        print("Progress won't be saved.")
        self.print_results(player=player)

    def get_user_answer(self, options: dict):
        question = 'What do you want to do?'
        while True:
            print(question)
            for key, value in options.items():
                print(f'{key}. {value}')
            answer = input(f'Select option number: ')
            if answer in options.keys():
                return answer
            print('Option number is invalid, please try again')

    def print_player_move(self, player: Player, monster: Monster):
        time.sleep(1)
        print('-----------------------------------')
        print('You meet monster on your way!!!')
        self.print_monster(monster=monster)
        print('Your statistics:')
        self.print_player(player=player)
        print('-----------------------------------')
        time.sleep(1)

    def print_player(self, player: Player):
        table = PrettyTable()
        table.field_names = ["Level", "Experience", "Level up exp", "Energy", "Defeated monsters"]
        table.add_row([
            player.level,
            player.experience,
            player.level_up_experience,
            player.energy,
            len(player.defeated_monsters)
        ])
        print(table)

    def print_monster(self, monster: Monster):
        table = PrettyTable()
        table.field_names = ["Monster name", "Gained experience", "Victory chance"]
        table.add_row([monster.name, monster.gained_exp, monster.victory_chance])
        print(table)

    def player_move_result(self, energy_points: int, is_victory: bool, is_run: bool, monster: Monster = None):
        energy_points = abs(energy_points)

        if is_run:
            text = f"You choose to run away. You loose {energy_points} energy points"
        else:
            text = (f"You couldn't defeat monster, but you can try again!!!\n"
                    f"You loose {energy_points} energy points")
            if is_victory:
                text = (f"Congrats!!! You win!!!\n"
                        f"You get {monster.gained_exp} exp points and loose {energy_points} energy points")

        time.sleep(1)
        print(text)
        time.sleep(1)

    def print_save_file_error(self, file: str):
        print(f"File {file} damaged or doesn't exist")
        print("You can't continue previous game")

    def print_monster_file_error(self, file: str):
        print(f"File {file} damaged or doesn't exist")
        print('Please wait, monsters file is been prepared')
