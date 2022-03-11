#Slice List between two indices exclusive of end index
listA = ['a', 'e', 'i', 'o', 'u','c', 'd', 'f']
Slice_Start=int(input("Enter the Slice Start index:"))
Slice_End=int(input("Enter the Slice End index:"))
listB=[listA[Slice_Start-1:Slice_End]]
print(listB)



