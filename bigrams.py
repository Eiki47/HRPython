from operator import itemgetter
import string
def open_file(file):
    try:
        strings = open(file, "r")
        return strings
    except FileNotFoundError:
        return None

def file_text_to_list(file):
    text = []
    for line in open_file(fileInp):
        for word in line.split():
            noPunc = word.strip(string.punctuation)
            text.append(noPunc.lower())
    return text

def createBigrams(text):
    bigrams={}
    for index in range(0, len(text)):
        if index != len(text) - 1:
            if (text[index], text[index + 1]) in bigrams:
                bigrams[(text[index], text[index + 1])] += 1
            else:
                bigrams[(text[index], text[index + 1])] = 1
    return bigrams

def sortBigram(bigram):
    sorted_d = sorted(bigram.items(), key=itemgetter(1,0))
    top_d = []
    for index in range(1, 11):
        top_d.append(sorted_d[-index])
    return top_d

fileInp=str(input("Enter name of file: "))
fileText = file_text_to_list(open_file(fileInp))
bigrams=createBigrams(fileText)
print(sortBigram(bigrams))
