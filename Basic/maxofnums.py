num1 = int(input("Enter first num "))
num2 = int(input("Enter second num "))

def maxofnums(num1, num2):
    try:
        return max(num1, num2)
    except Exception as e:
        print("An exception occured")

print("Max is "+ str(maxofnums(num1, num2)))


