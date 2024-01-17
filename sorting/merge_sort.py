def merge_sort(array):
    mid = len(array) // 2

    left_array = array[:mid]
    right_array = array[mid:]

    # recursion
    merge_sort(left_array)
    merge_sort(right_array)

    left = 0
    right = 0
    k = 0

    while left < len(left_array) and right_array < len(right_array):
        if left_array[left] < right_array[right]:
            array[k] = left_array[left]
            left += 1
        else:
            array[k] = right_array[right]
            right += 1
        k += 1

    while left < len(left_array):
        array[k] = left_array[left]
        left += 1
        k += 1

    while right < len(right_array):
        array[k] = right_array[right]
        right += 1
        k += 1
