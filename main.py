
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


def create_monsters_file():
    response = requests.get(MONSTER_FILE_URL)
    data = response.json()

    with open(MONSTER_FILE, "w") as outfile:
        json.dump(data, outfile, indent=2)


def file_settings(interface: Interface):

    if not check.is_file_available(file=MONSTER_FILE):
        interface.print_monster_file_error(file=MONSTER_FILE)
        create_monsters_file()

    if not check.is_file_available(file=SAVE_FILE):
        interface.print_save_file_error(file=SAVE_FILE)
        interface.player_menu_options.pop('2')


def main():
    interface = Interface()
    interface.greeting()
    file_settings(interface)
    answer = interface.get_user_answer(interface.player_menu_options)
    player = Player()
    if answer == '3':
        sys.exit(0)
    elif answer == '2':
        player.load_player_data()
    game = Game(player=player, interface=interface)
    game.start_game()


if __name__ == '__main__':
    main()
