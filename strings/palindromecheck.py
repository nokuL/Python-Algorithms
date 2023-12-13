def palindromecheck(string):
    """function to check if num is palindrome or not"""
    # using two pointer technique
    left_pointer = 0
    right_pointer = len(string) - 1

    while left_pointer <= right_pointer:
        if string[right_pointer] == string[left_pointer]:
            left_pointer += 1
            right_pointer -= 1
            if left_pointer == right_pointer:
                return True
        else:
            return False


print(palindromecheck("bobb"))
