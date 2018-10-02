import string
#build_wordlist() function goes here
def build_wordlist(file):
    newString=""
    for line in file:
        for letter in line:
            if letter not in string.punctuation:
                newString+=letter
    newStringToList = newString.split()
    return newStringToList
#find_unique() function goes here
def find_unique(word_list):
    uniqueList=[]
    for word in word_list:
        if word not in uniqueList:
            uniqueList.append(word)
    return uniqueList
def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)
    infile.close()
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()
