"""Create initial game data for specified number of players"""

import random
import math
import pandas as pd

players = pd.DataFrame(columns=['username', 'posX', 'posY', 'hp', 'range', 'ap', 'dead'])
PLAYER_SPACE = 20
player_max = int(input("Total number of players: "))
field_size = math.ceil((player_max * PLAYER_SPACE) ** (1/2))

while len(players) < player_max:
    player_num = len(players)
    uname = input(f'Username for Player {player_num + 1}: ')
    if uname == "":
        continue

    done = False
    while not done:
        x_pos = random.randint(0, field_size)
        y_pos = random.randint(0, field_size)

        repeated = players.loc[((players['posX'] == x_pos) & (players['posY'] == y_pos))]

        if len(repeated) == 0:
            done = True

    players.loc[len(players.index)] = [uname, x_pos, y_pos, 3, 2, 1, False]

print(players)
players.to_csv('playerData.csv', index=False)
