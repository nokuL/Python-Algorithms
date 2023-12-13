def rotatearray(array, k):
    """rotate array by k elements"""
    #using multiple reversal technique for all elements
    # using inplace reverseal technique
    k = k % len(array)
    
    start = 0
    end = len(array)-1
    array = reversearrayutil(array, start, end)

    k= k-1
    start = 0
    end = k
    array=reversearrayutil(array, start, end)

    start = k+1
    end= len(array)-1
    array= reversearrayutil(array, start, end)

    return array


def reversearrayutil(array, start, end):
     while start <= end:
        array[start], array[end] = array[end], array[start]
        start+=1
        end-=1
     return array

print(rotatearray([1,2,3,4,5,6,7], 3))