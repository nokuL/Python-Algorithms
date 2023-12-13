def largestnuminarray(array):
    max = 0
    for num in array:
        max = max(max, num)
    return max


def largestnum_twopointer(array):
    if not array:
        return None

    left_pointer = 0
    right_pointer = len(array)-1
    max_num = 0

    for num in array:
        max_num = max(max_num, array[left_pointer], array[right_pointer])
        left_pointer +=1
        right_pointer -=1
    
    return max_num

array = [1,2, 3, 4, 5]
print(largestnum_twopointer(array))