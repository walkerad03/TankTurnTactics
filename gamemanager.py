#!/usr/bin/python
import json


class GameManager():
    def __init__(self, playerlist) -> None:
        self.playerlist = playerlist

    def handle_move(self, selected_move):
        if selected_move == "shoot":
            print('Selected shoot')
        elif selected_move == "move":
            print('Selected move')
        elif selected_move == "range":
            print('Selected range')
            for player in self.playerlist:
                if player['isClient'] and player['ap'] > 3:
                    player['range'] += 1
                    player['ap'] -= 3
        elif selected_move == "heal":
            print('Selected Heal')
            for player in self.playerlist:
                if player['isClient'] and player['ap'] > 3:
                    if player['hp'] < 3:
                        player['hp'] += 1
                        player['ap'] -= 3
        elif selected_move == "transfer":
            print('Selected Transfer')

        return json.dumps(self.playerlist)
