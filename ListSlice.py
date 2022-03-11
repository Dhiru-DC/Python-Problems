#List Slice

listA = ['a', 'e', 'i', 'o', 'u','c', 'd', 'f']
Slice=int(input("Enter the first sublist length:"))
listB=[]
i=0
if(Slice > len(listA)):
    print("Enter Valid Input/List Size is low")
else:
    while i < (Slice):
        listB.append(listA[0])
        listA.pop(0)
        i+=1
    print("Sliced list are:({} {})".format(listB,listA))



