import pandas as pd
import random
import math

players = pd.DataFrame(columns=['username', 'posX', 'posY', 'hp', 'range', 'ap', 'dead'])
player_space = 20
player_max = int(input("Total number of players: "))
field_size = math.ceil((player_max * player_space) ** (1/2))

while len(players) < player_max:
    player_num = len(players)
    uname = input('Username for Player {} (Leave blank to end): '.format(player_num + 1))
    if uname == "":
        break

    done = False
    while(not done):
        xPos = random.randint(0, field_size)
        yPos = random.randint(0, field_size)

        repeated = players.loc[((players['posX'] == xPos) & (players['posY'] == yPos))]

        if(len(repeated) == 0):
            done = True

    players.loc[len(players.index)] = [uname, xPos, yPos, 3, 2, 1, False]

print(players)
players.to_csv('playerData.csv', index=False)
