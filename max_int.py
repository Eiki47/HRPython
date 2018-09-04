max_int=0
while True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int < 0: #Segir til ef inputtið er mínus tala og stoppar þá while loopuna
        break 
    else:
        if num_int > max_int: #Athugar ef inputtið er það stærsta sem hefur verið inputtað
            max_int = num_int #Gerir inputtið að stærstu tölunni
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line


