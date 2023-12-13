
def sumofarray(array):
    """function to calculate summ of array"""
    sum =0
    for num in array:
        sum+=num
    return sum


def sumofarray2(array):
    """function to calculate sum of array 2"""
    return sum(array)

def sumofarray_twopointer(array):
    if not array:
        return None
    
    if len(array)== 1:
        return array[0]
    

    left_pointer = 0
    right_pointer = len(array)-1
    sum_num = 0
    
    while left_pointer <= right_pointer:
        sum_num = sum_num + array[left_pointer] + array[right_pointer]
    return sum_num



array = [1,2, 3, 4, 5]
print(sumofarray2(array))