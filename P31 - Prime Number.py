# P31 Prime Number Test

import math as m

# Custom Error For negative numbers
class Error(Exception):
    pass


class invalidinputError(Error):
    pass


def isPrime(num):
    try:
        if (num % 2 == 0):
            return 0
        else:
            root = m.ceil(m.sqrt(num))
        for i in range(2, root + 1):
            if (num % i == 0):
                return 0
        return 1
    except:
        print("Enter valid number")


sample = int(input("Enter the number to be tested:"))

try:
    if sample < 1:
        raise invalidinputError
    else:
        if isPrime(sample):
            print("{} is prime number".format(sample))
        else:
            print("{} is not a prime number".format(sample))
except invalidinputError:
    print("Enter Valid Input")

