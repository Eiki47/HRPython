#Forritið keyrist á while loopu alveg upp að þeim tímapunkti þegar notandi vinnur leikinn á reit 3,1.
#Við látum öll tile-in í sér breytur sem inniheldur sérhverja átt fyrir þann reit.

tile11 = "N"
tile12 = "NES"
tile13 = "SE"
tile21 = "N"
tile22 = "SW"
tile23 = "EW"
tile32 = "NS"
tile33 = "SW"

player_tile_x=1
player_tile_y=1

possibilites = ""

victory = False
while victory == False:   
    if player_tile_x == 1 and player_tile_y == 1: possibilites = tile11
    if player_tile_x == 1 and player_tile_y == 2: possibilites = tile12
    if player_tile_x == 1 and player_tile_y == 3: possibilites = tile13
    if player_tile_x == 2 and player_tile_y == 1: possibilites = tile21
    if player_tile_x == 2 and player_tile_y == 2: possibilites = tile22
    if player_tile_x == 2 and player_tile_y == 3: possibilites = tile23
    if player_tile_x == 3 and player_tile_y == 2: possibilites = tile32
    if player_tile_x == 3 and player_tile_y == 3: possibilites = tile33
