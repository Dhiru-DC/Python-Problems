# P34 Finding Eulor's totient using GCD function

def phi(m):
    count =0;
    if m==1:
        return 1
    for i in range(1,m):
        if GCD(i,m)==1:
            count +=1
    return count

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



Num_1=int(input("Enter the Number: "))

print(phi(Num_1))




