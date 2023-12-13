def splitfirstpart(array, k):
    """function to split the first part of array from n to k-1"""
    #k-1 because fof zero indexing

    start = 0
    end= len(array)-1

    #reverse the whole array
    array = reversearray(array, start, end)

    #reverse first part
    start = 0
    end = (len(array)-k)-1
    array = reversearray(array, start, end)

    #rerse last part
    start = len(array)-k
    end = len(array)-1
    array = reversearray(array, start, end)
    return array





def reversearray(array, start, end):
    while start<= end:
        array[start], array[end]= array[end], array[start]
        start+=1
        end-=1
    return array


print(splitfirstpart([12,10, 5, 6, 52, 36], 2))
