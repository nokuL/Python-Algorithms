def last_duplicate_el(array):
    if len(array) == 0:
        raise ValueError("Invalid array length")

    # sort array first
    array = array.sort()

    n = len(array) - 1

    while n > 0:
        if array[n] == array[n - 1]:
            print("Array index :", n)
            print("Array element :", n - 1)
            return
        n -= 1
    print("No duplicates found")
