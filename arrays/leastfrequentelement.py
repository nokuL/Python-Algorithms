def leastFrequentElement(array):
    """function to check least frequent element in an array"""

    min_count = 1000000000
    dictionary = {}
    res = array[0]

    for i in range(1, len(array)):
        if array[i] in dictionary:
            dictionary[array[i]] += 1
        else:
            dictionary[array[i]] = 1

        if dictionary[array[i]] < min_count:
            min_count = dictionary[array[i]]
            res = array[i]
    return res
