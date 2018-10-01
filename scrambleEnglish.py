import random
import string

def handle_punctuation(word):
    string_to_list = list(word)
    list_to_scramble = string_to_list[1:-1]
    random.shuffle(list_to_scramble)
    new_word = word[0] + ''.join(list_to_scramble) + word[-1]
    punctation_word_list = list(new_word)
    return ''.join(punctation_word_list)


def word_string_to_list(word_string):
    split_string = word_string.split()
    return split_string

def scramble_string(word_string):
    word_list = word_string_to_list(word_string)
    new_word_list=[]
    for word in word_list:
        if len(word) > 4:
            if [letter for letter in word if letter in string.punctuation]:
                new_word_list.append(handle_punctuation(word))
            else:
                string_to_list = list(word)
                list_to_scramble = string_to_list[1:-1]
                random.shuffle(list_to_scramble)
                new_word = word[0]+''.join(list_to_scramble)+word[-1]
                new_word_list.append(new_word)
        else:
            new_word_list.append(word)
    return ' '.join(new_word_list)

def get_word_string(file):
    try:
        with open(file, "r") as file_strings:
            strings = file_strings.readlines()
        return ''.join(strings)
    except FileNotFoundError:
        print ("File",file,"not found")
        return ""

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)
