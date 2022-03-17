# P41 Goldbach's conjecture list
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


def Conjecture(lower,upper):
    modified_list=[] # list for cnumber where both the primes are greater than 50
    print("Conjecture list")
    if lower%2!=0:
        lower += 1
    for i in range(lower,upper+1,2):
        n=3
        while True:
            if isPrime(n) and isPrime(i - n):
                print(n, i - n, sep=" ")
                if n > 50 and (i-n) > 50:
                    modified_list.append([n,i-n])
                break
            else:
                n += 2
    print("Primes greater than 50")
    for j in modified_list:
        print(j)
    return 1


lower,upper = (input("Enter the Lower and Upper Limit ( Note: Lower limit should be greater than 4 whereas upper limit should be greater than 5) : ")).split()
lower=int(lower)
upper=int(upper)
try:
    if lower>4 and upper>5:
        Conjecture(lower,upper)
    else:
        raise ValidNumberError
except ValidNumberError:
    print("Invalid Range Entered")
