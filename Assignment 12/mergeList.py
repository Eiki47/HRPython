def merge_lists(list1, list2):
    mergedList = list(set().union(list1, list2))
    return sorted(mergedList)

# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
