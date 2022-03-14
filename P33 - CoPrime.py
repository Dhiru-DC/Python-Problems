# P33 GCD Using Euclid's algorithm and Co prime test

def GCD(Num1,Num2): #Recursive Function to Find GCD
    if Num1==0 or Num2==0:
        if Num1==0:
         return Num2
        else:
            return Num1
    else:
        if Num1>Num2:
            remainder=Num1%Num2
            return GCD(Num2,remainder)
        else:
            remainder=Num2%Num1
            return GCD(Num1,remainder)



Num_1,Num_2=input("Enter Space separated two numbers: ").split()

if GCD(abs(int(Num_1)),abs(int(Num_2)))==1: # If GCD is 1 then numbers are coprime else not
    print("{} and {} are coprime".format(Num_1,Num_2))
else:
    print("{} and {} are not coprime".format(Num_1,Num_2))



