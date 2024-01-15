def majorityElement(array):
    """function to find the majority element """
    majority_el = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] != majority_el:
            count -= 1
            if count == 0:
                majority_el = array[i]
                count += 1  # Update majority element candidate
        else:
            count += 1

    # At this point, majority_el represents a potential majority element
    # We need to verify if it occurs more than n/2 times in the array
    count = 0
    for num in array:
        if num == majority_el:
            count += 1

    if count > len(array) // 2:
        return majority_el
    else:
        return None
