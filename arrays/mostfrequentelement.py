def mostfrequentel(array):
    if len(array) == 0:
        raise ValueError("Invalid array length")

    # first sort elements
    array = array.sort()

    curr_count = 1
    max_count = 1
    res = array[0]

    for i in (1, len(array)):
        if array[i] == array[i - 1]:
            curr_count += 1
        else:
            curr_count = 1

        if curr_count > max_count:
            max_count = curr_count
            res = array[i]

    return res


def mostFreqEl2(array):
    """using dictionary and looping once"""
    # no sorting firstd
    dict = {}
    max_count = 1
    curr_count = 1
    result = array[0]

    for i in range(1, len(array)):
        if array[i] in dict:
            dict[array[i]] += 1
        else:
            dict[array[i]] = 1

        if dict[array[i]] > max_count:
            max_count = dict[array[i]]
            result = array[i]
    return result


def checkMostFreq():
    print(mostfrequentel([1, 1, 3, 4, 1, 7]))
