#Forritið keyrist á while loopu alveg upp að þeim tímapunkti þegar notandi vinnur leikinn á reit 3,1.
#Við látum öll tile-in í sér breytur sem inniheldur sérhverja átt fyrir þann reit.
#https://github.com/Eiki47/HRPython/tree/master/TileTraveller
#1. Which implementation was easier and why?
#Það er án efa einfaldara að gera forritið án þess að nota föll, maður áttar sig betur á
#flæðinu í forritinu og uppsetningin er einföld
#2. Which implementation is more readable and why?
#Hins vegar er mikið þægilegra að lesa kóðann með föllum og nöfnin á föllunum gefur fólki hugmynd um hvað
#forritið er að gera skref fyrir skref.
#3. Which problems in the first implementations were you able to solve with the latter implementation?
#Ég gat sett möguleikana saman í eitt fall sem lýtur betur út og einfaldar forritið.
def possib(x,y):
    possibilites = ""
    tile11 = "(N)orth."
    tile12 = "(N)orth or (E)ast or (S)outh."
    tile13 = "(E)ast or (S)outh."
    tile21 = "(N)orth."
    tile22 = "(S)outh or (W)est."
    tile23 = "(E)ast or (W)est."
    tile32 = "(N)orth or (S)outh."
    tile33 = "(S)outh or (W)est."
    if player_tile_x == 1 and player_tile_y == 1: possibilites = tile11
    if player_tile_x == 1 and player_tile_y == 2: possibilites = tile12
    if player_tile_x == 1 and player_tile_y == 3: possibilites = tile13
    if player_tile_x == 2 and player_tile_y == 1: possibilites = tile21
    if player_tile_x == 2 and player_tile_y == 2: possibilites = tile22
    if player_tile_x == 2 and player_tile_y == 3: possibilites = tile23
    if player_tile_x == 3 and player_tile_y == 2: possibilites = tile32
    if player_tile_x == 3 and player_tile_y == 3: possibilites = tile33
    return possibilites

def victoryCheck(x,y):
    if x == 3 and y == 1:
        print("Victory!")
        return True

def directions(dir, x, y):
    if (dir == "N" or dir == "n") and "(N)orth" in possib(x, y):
        y += 1
        validation = True
    elif (dir == "E" or dir == "e") and "(E)ast" in possib(x, y):
        x += 1
        validation = True
    elif (dir == "S" or dir == "s") and "(S)outh" in possib(x, y):
        y -= 1
        validation = True
    elif (dir == "W" or dir == "w") and "(W)est" in possib(x, y):
        x -= 1
        validation = True
    else:
        print ("Not a valid direction!")
        validation = False
    return x,y, validation

player_tile_x=1
player_tile_y=1
valid = 0
victory = False
validation = True
while victory == False:
    if victoryCheck(player_tile_x, player_tile_y):
        break
    else:
        if validation:
            print ("You can travel:", possib(player_tile_x, player_tile_y))
        direc = str(input("Direction: "))
        player_tile_x, player_tile_y, validation = directions(direc, player_tile_x, player_tile_y)

