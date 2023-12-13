def reversearray(array):
    """function to rotate array"""
    #accept array
    #find middle index 
    #swap elements in left and right index
    #use two pointer technique

    if len(array) == 0:
        return None
    elif len(array)== 1:
        return array
    else:
        left_pointer = 0
        right_pointer = len(array)-1

        while left_pointer <= right_pointer:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]
            left_pointer+=1
            right_pointer-=1
        return array

            
print(reversearray([1,2,3,4,5, 6,7]))
