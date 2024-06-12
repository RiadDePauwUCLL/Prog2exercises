def findMaximum(list):
    if len(list) == 0:
        raise IndexError
    # Base case: if the list has only one item, return that item
    if len(list) == 1:
        return list[0]

    # Recursive case: compare the first element to the maximum of the rest of the list
    else:
        max_of_rest = findMaximum(list[1:])
        return list[0] if list[0] > max_of_rest else max_of_rest

