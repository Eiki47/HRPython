#Forritið keyrist á while loopu alveg upp að þeim tímapunkti þegar notandi vinnur leikinn á reit 3,1.
#Við látum öll tile-in í sér breytur sem inniheldur sérhverja átt fyrir þann reit.

tile11 = "(N)orth"
tile12 = "(N)orth or (E)ast or (S)outh"
tile13 = "(S)outh or (E)ast"
tile21 = "(N)orth"
tile22 = "(S)outh or (W)est"
tile23 = "(E)ast or (W)est"
tile32 = "(N)orth or (S)outh"
tile33 = "(S)outh or (W)west"

player_tile_x=1
player_tile_y=1

possibilites = ""

victory = False
while victory == False:
    if player_tile_x == 3 and player_tile_y == 1:
        print("Victory!")
        victory = True
    else:
        if player_tile_x == 1 and player_tile_y == 1: possibilites = tile11
        if player_tile_x == 1 and player_tile_y == 2: possibilites = tile12
        if player_tile_x == 1 and player_tile_y == 3: possibilites = tile13
        if player_tile_x == 2 and player_tile_y == 1: possibilites = tile21
        if player_tile_x == 2 and player_tile_y == 2: possibilites = tile22
        if player_tile_x == 2 and player_tile_y == 3: possibilites = tile23
        if player_tile_x == 3 and player_tile_y == 2: possibilites = tile32
        if player_tile_x == 3 and player_tile_y == 3: possibilites = tile33
        print ("You can travel: ", possibilites)
        direc = str(input("Direction: "))

        if (direc == "N" or direc == "n") and "(N)orth" in possibilites:
            player_tile_y += 1
        elif (direc == "E" or direc == "e") and "(E)ast" in possibilites:
            player_tile_x+=1
        elif (direc == "S" or direc == "s") and "(S)outh" in possibilites:
            player_tile_y -= 1
        elif (direc == "W" or direc == "w") and "(W)est" in possibilites:
            player_tile_x -= 1
        else:
            print ("Not a valid direction!")
