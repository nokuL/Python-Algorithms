

def armstrongcheck(num):
    """function to check if num is armstrong number"""
    number_string = str(num)
    order = len(number_string)
    sum = 0
    originalnum = num

    while num>0:
        digit = num%10
        sum+= digit ** order
        num = num//10
    
    if originalnum == sum:
        return True
    else :
        return False


def armstrongcheck2(num):
    """function to check if num is armstrong number using string"""

    order = len(num)
    sum = 0
    for digit in num:
        sum += int(digit)**order

    if int(num) == sum:
        return True
    else:
        return False


def armstrong_twopointer(num):
    order = len(num)
    sum = 0
    left_pointer = 0
    right_pointer = len(num)-1

    while left_pointer <= right_pointer:
        sum = int(num[left_pointer])**order +int(num[right_pointer])**order
        print(sum)
        print(num)
        left_pointer +=1
        right_pointer -=1
    if sum == num:
        return True
    else:
        return False


num = input("Enter number :")
print(armstrong_twopointer(num))