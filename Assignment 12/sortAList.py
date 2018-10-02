# sort_list() function goes here
def sort_list(list):
    list.sort()
def main():
    # loop to accept integers until a non-digit is entered goes here
    a_list = []
    while True:
        digit_input=input()
        try:
            digit = int(digit_input)
            a_list.append(digit)
        except ValueError:
            break

    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######


main()
