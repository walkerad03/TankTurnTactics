#!/usr/bin/python
import json
import pandas as pd
class GameManager():
    def __init__(self, playerlist) -> None:
        self.playerlist = playerlist

    def handle_move(self, selected_move):
        if (selected_move == "shoot"):
            pass
        elif (selected_move == "move"):
            pass
        elif (selected_move == "range"):
            for player in self.playerlist:
                if(player['isClient'] and player['ap'] > 3):
                    player['range'] += 1
                    player['ap'] -= 3
        elif (selected_move == "heal"):
            for player in self.playerlist:
                if(player['isClient'] and player['ap'] > 3):
                    if(player['hp'] < 3):
                        player['hp'] += 1
                        player['ap'] -= 3
        elif (selected_move == "transfer"):
            pass

        return json.dumps(self.playerlist)
