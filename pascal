def make_new_row(row):
    n=len(row)
    row.append([])
    row[i].append(1)
    for j in range(1,i):
        row[i].append(row[i-1][j-1]+row[i-1][j])
    if(n!=0):
        row[i].append(1)
    print(row[-1])
    return row
# Main program starts here - DO NOT CHANGE
height = int(input("Height of Pascal's triangle (n>=1): "))
new_row = []
for i in range(height):
    new_row = make_new_row(new_row)
