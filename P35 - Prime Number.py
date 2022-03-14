#P35 Prime Factors of a number
import math as m

# Custom Error For negative numbers

def isPrime(num):
    if num==2:
        return 1
    elif num % 2 == 0:
            return 0
    else:
            root = m.ceil(m.sqrt(num))
    for i in range(2, root + 1):
            if (num % i == 0):
                return 0
    return 1

Sample_List=[]


def PrimeFactors(m):
    n=2
    while n<=m:
        if m%n==0 and isPrime(n)==1:
            Sample_List.append(n)
            m = m//n
        else:
            if n==2:
                n+=1
            else:
                n+=2
    return 1



num=int(input("Enter the Number: "))
PrimeFactors(num)
print(Sample_List)
