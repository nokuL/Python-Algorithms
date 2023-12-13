num1 = int(input("Enter 1st number :"))

num2 = int(input("Enter 2nd number :"))

def addtwonums(num1, num2):
    """ a function to add two numbers"""
    try:
        result = num1 + num2
        return result
    except ValueError as e:
        print("Could not add because of "+ str(e))


result = addtwonums(num1, num2)

print("The result is :  "+ str(result))

