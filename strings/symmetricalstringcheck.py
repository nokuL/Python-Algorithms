def symmetrical_string_check(string):
    """function to check if string is symmetrical or not"""
    mid_index = len(string) // 2
    first_str = string[:mid_index]
    second_str = string[mid_index+1:]

    if first_str == second_str[::-1]:
        return True
    else:
        return False

# Test the function
print(symmetrical_string_check("abcba"))   # True
print(symmetrical_string_check("hello"))