#!/usr/bin/python

class GameManager():
    def __init__(self, playerlist) -> None:
        self.playerlist = playerlist

    def handle_move(self, selected_move):
        if (selected_move == "shoot"):
            print("Shoot has been selected")
        elif (selected_move == "move"):
            print("Move has been selected")
        elif (selected_move == "range"):
            print("Range has been selected")
            for player in self.playerlist:
                if(player['isClient'] and player['ap'] > 3):
                    player['range'] += 1
                    player['ap'] -= 3
        elif (selected_move == "heal"):
            print("Heal has been selected")
        elif (selected_move == "transfer"):
            print("Transfer has been selected")

        return self.playerlist
