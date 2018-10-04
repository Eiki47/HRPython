# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'


def move(direction, col, row):
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return (col, row)


def is_victory(col, row):
    return col == 3 and row == 1  # (3,1)


def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")


def find_directions(col, row):
    if col == 1 and row == 1:  # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2:  # (1,2)
        valid_directions = NORTH + EAST + SOUTH
    elif col == 1 and row == 3:  # (1,3)
        valid_directions = EAST + SOUTH
    elif col == 2 and row == 1:  # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2:  # (2,2)
        valid_directions = SOUTH + WEST
    elif col == 2 and row == 3:  # (2,3)
        valid_directions = EAST + WEST
    elif col == 3 and row == 2:  # (3,2)
        valid_directions = NORTH + SOUTH
    elif col == 3 and row == 3:  # (3,3)
        valid_directions = SOUTH + WEST
    return valid_directions

def check_for_lever(col, row):
    if col == 1 and row == 2:
        lever = True
    elif col == 2 and row == 2:
        lever = True
    elif col == 2 and row == 3:
        lever = True
    elif col == 3 and row == 2:
        lever = True
    else:
        lever = False
    return lever

def lever_choice(coins):
    local_coins = coins
    lever_input = str(input("Pull a lever (y/n): "))
    if lever_input == "y" or lever_input == "Y":
        local_coins += 1
        print("You received 1 coins, your total is now " + str(local_coins) + ".")
        return 1
    elif lever_input == "n" or lever_input == "N":
        return 0
    else:
        print ("Not a valid input!")
        return 0

# The main program starts here
victory = False
row = 1
col = 1
lever = False
coins = 0

valid_directions = NORTH
print_directions(valid_directions)

while not victory:
    direction = input("Direction: ")
    direction = direction.lower()

    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        if victory:
            print("Victory!")
        else:
            if check_for_lever(col, row):
                coins += lever_choice(coins)
            valid_directions = find_directions(col, row)
            print_directions(valid_directions)
