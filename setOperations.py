list1 = str(input("Input a list of integers separated with a comma: ")).split(",")
list2 = str(input("Input a list of integers separated with a comma: ")).split(",")

intList1=numbers = list(map(int, list1))
intList2=numbers = list(map(int, list2))

set1 = set(intList1)
set2 = set(intList2)
print (set1)
print (set2)

while True:
    print ("1. Intersection\n2. Union\n3. Difference\n4. Quit")
    setOp = int(input("Set operation: "))
    if setOp == 1:
        print (set1 & set2)
    elif setOp == 2:
        print (set1 | set2)
    elif setOp == 3:
        print (set1 - set2)
    elif setOp == 4:
        break
