#For loopa sem keyrir n sinnum fyrir hverja einustu tölu
#Forritið athugar fyrst ef n er 1,2 eða 3 og svo prentar einfaldleg út niðurstöðuna frá þeim caseum
#Annars bætir það tölum í lista til að halda utan um síðustu þrjár tölurnar
#Forritið tekur summuna á listanum og bætir henni við listan og á sama tíma fjarlægir fyrstu töluna.
#Annar listi heldur utan um allar tölur alveg upp að sequenceið er búið
n = int(input("Enter the length of the sequence: ")) # Do not change this line
x=[1,2,3]
total_x=["1","2","3"]
if n == 1:
    print(x[0])
elif n == 2:
    print(x[0:2])
elif n == 3:
    print(x[0:3])
for i in range(n-3):
    new_nr = sum(x)
    total_x.append(str(new_nr))
    x.append(new_nr)
    x.pop(0)
for j in total_x:
    print (j)
