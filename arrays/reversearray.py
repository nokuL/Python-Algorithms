def reverse_array(array):
    """Function to reverse an array"""
    # using swapping method
    if len(array) == 0:
        raise ValueError("Invalid array length this one")
    start = 0
    end = len(array) - 1
    while start <= end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

