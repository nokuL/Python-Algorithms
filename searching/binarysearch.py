def binarysearch(array, num, left, right):
    """Function to perform a binary search on an array using the recursion technique"""
    # ensure the array is sorted

    array.sort()
    mid = (left + right) // 2
    if left > right:
        return False

    if array[mid] == num:
        return True
    elif num > array[mid]:
        return binarysearch(array, num, mid + 1, right)
    else:
        return binarysearch(array, num, left, mid - 1)

