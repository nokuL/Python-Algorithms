def left_rotate_array(array, k):
    """function to left rotate an array"""
    # firt use % to make sure length of array is greater than k

    k = k % len(array)

    # rotate all elements
    start = 0
    end = len(array) - 1
    array = reverse_util(array, start, end)

    # rotate last 2 elements
    start = end - k
    array = reverse_util(array, start, end)

    # rotate the first elements
    start = 0
    end = (len(array) - 1) - (k + 1)
    array = reverse_util(array, start, end)

    return  array


def reverse_util(array, start, end):
    while start <= end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array
