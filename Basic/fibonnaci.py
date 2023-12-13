def fibonacci(n):
    """finding the nth value in a fibonacci series"""
    #base case 
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n < 1:
        return 0
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

print(fibonacci(8))