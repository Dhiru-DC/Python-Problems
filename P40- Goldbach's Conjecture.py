# P40 Goldbach's conjecture
import math as m


# Custom Error For Invalid numbers

class Error(Exception):
    pass

class ValidNumberError(Error):
    pass

def isPrime(num):
    if num == 2:
        return 1
    elif num % 2 == 0:
        return 0
    else:
        root = m.ceil(m.sqrt(num))
    for i in range(2, root + 1):
        if (num % i == 0):
            return 0
    return 1


def Conjecture(m):
    n = 3
    while True:
        if isPrime(n) and isPrime(m - n):
            print(n, m - n, sep=" ")
            break
        else:
            n += 2

    return 1


num = int(input("Enter the Number: "))
try:
    if num%2==0 and num > 2:
        Conjecture(num)
    else:
        raise ValidNumberError
except ValidNumberError:
    print("Invalid Number Entered")
