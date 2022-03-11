#List Rotate

listA = ['a', 'e', 'i', 'o', 'u','c', 'd', 'f']
Slice=int(input("Enter the Rotate Factor:"))
listB=[]
i=0
if(Slice > len(listA)):
    print("Enter Valid Input/List Size is low")
else:
    while i < (Slice):
        listB.append(listA[0])
        listA.pop(0)
        i+=1
listA.extend(listB)
print("Rotated list is: {}".format(listA))



