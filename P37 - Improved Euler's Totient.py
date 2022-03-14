#P37 Euler's Totient improved
import math as m


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

def phi(Dict1):
    product=1
    for i in Dict1:
        product = product * ((i-1) *i ** (Dict1[i]-1))
    return product

Sample_Dict={}


def PrimeFactors(m):
    n=2
    while n<=m:
        if m%n==0 and isPrime(n)==1:
            if n in Sample_Dict:
                Sample_Dict[n] +=1
            else:
                Sample_Dict[n]=1
            m = m//n
        else:
            if n==2:
                n+=1
            else:
                n+=2
    return 1



num=int(input("Enter the Number: "))
PrimeFactors(num)
print(phi(Sample_Dict))
