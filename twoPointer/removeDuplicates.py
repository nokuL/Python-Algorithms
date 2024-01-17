def removeDuplicates(array):
    """This function removes dups from an array that is sorted"""

    left = 1
    for i in range(1, len(array)):
        if array[i] != array[i - 1]:
            array[left] = array[i]
            left += 1

    return left
