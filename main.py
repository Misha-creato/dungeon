import sys
import json
import check
import requests

from game import Game
from player import Player
from interface import Interface

from constants import (
    SAVE_FILE,
    MONSTER_FILE,
    MONSTER_FILE_URL,
)


def fix_save_file_settings(interface: Interface):
    interface.print_save_file_error(file=SAVE_FILE)
    interface.player_menu_options.pop('2')


def get_monsters_file():
    response = requests.get(MONSTER_FILE_URL)
    data = response.json()

    with open(MONSTER_FILE, "w") as outfile:
        json.dump(data, outfile, indent=2)


def fix_file_settings(interface: Interface):

    if not check.is_file_available(file=MONSTER_FILE):
        interface.print_monster_file_error(file=MONSTER_FILE)
        get_monsters_file()

    if not check.is_file_available(file=SAVE_FILE):
        fix_save_file_settings(interface=interface)


def get_player(interface: Interface):
    save_loaded = False
    while not save_loaded:
        answer = interface.get_user_answer(interface.player_menu_options)
        if answer == '1':
            player = Player()
            save_loaded = True
        elif answer == '2':
            player = Player()
            save_loaded = player.load_player_data()
            if not save_loaded:
                fix_save_file_settings(interface=interface)
        else:
            interface.print_results()
            sys.exit(0)
    return player


def main():
    interface = Interface()
    interface.greeting()
    fix_file_settings(interface)
    player = get_player(interface=interface)
    game = Game(player=player, interface=interface)
    game.start_game()


if __name__ == '__main__':
    main()
