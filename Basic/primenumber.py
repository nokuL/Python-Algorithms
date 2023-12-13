def primenumbercheck(num):
    flag = False
    for i in range (2, num):
        if num % i == 0:
            flag = True
            break
    if flag:
        print("Num is not a prime number")
    else: 
        print("Num a prime number")


primenumbercheck(29)