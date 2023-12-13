def monotoniccheck(array):
    if len(array)==0:
        raise ValueError("Invalid argument")
    if len(array)==1:
        return True
    return (all(array[i]< array[i+1] for i in range(len(array)-1)) or 
            all(array[i]>array[i+1] for i in  range(len(array)-1)))

