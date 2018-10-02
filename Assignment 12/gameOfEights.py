#game_of_eights() function goes here
def game_of_eights(list):
    letterCheck = [letter for letter in list if letter.isalpha()]
    if len(letterCheck) > 0:
        return "Error. Please enter only integers."
    else:
        idx = 0
        for number in list:
            if idx+1 == len(list):
                return False
            elif int(number) == 8 and int(list[idx+1]) == 8:
                return True
            idx += 1
        return False
def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    print (game_of_eights(a_list))
main()
