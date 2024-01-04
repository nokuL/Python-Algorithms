def rotate_array(array, k):
    """function to reverese array by k"""
    # first % to make sure k is smaller than length of array
    k = k % len(array)

    # first rotate the whole array
    start = 0
    end = len(array)
    array = reverse_util(array, start, end)

    # next rotate the first k elements
    start = 0
    k = k - 1
    array = reverse_util(array, start, k)

    # reverse the remaining elements
    start = k + 1
    end = len(array) - 1
    array = reverse_util(array, start, end)


def reverse_util(array, start, end):
    while start <= end:
        array[end], array[start] = array[start], array[end]
        start += 1
        end -= 1
    return array
