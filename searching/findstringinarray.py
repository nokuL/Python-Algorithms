def findStringInArray(array, string, left, right):
    """function to find string in array"""

    mid = (left + right) // 2

    if left > right:
        return False
    if string == array[mid]:
        print("Array index is " + mid)
        return True
    elif string > array[mid]:
        return findStringInArray(array, string, mid + 1, right)
    else:
        return findStringInArray(array, string, left, mid - 1)
