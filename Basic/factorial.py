
def factorialBruteForce(num1):
    """Finding factorial of a number"""
    6*5*4*3*1
    fact = 1
    if num1 <0:
        return 0
    elif num1==0  or num1==1:
        return 1
    else:
        while(num1 > 1):
            fact = fact * num1
            num1-=1
    return fact


def factorialRecursion(num1):
    """finding factorial using recursion"""
    return 1 if (num1==1 or num1==0) else num1 * factorialRecursion(num1 - 1) 
    
print(factorialBruteForce(6))
print(factorialRecursion(6))

