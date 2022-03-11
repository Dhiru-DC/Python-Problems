#Insert element at Kth position from the list

listA = ['a', 'e', 'i', 'o', 'u','c', 'd', 'f']
position,data=input("Enter the Index of element and data to be entered into the list:").split()
if int(position)>len(listA)+1:
    print("Invalid index")
    print("Failed to add Element, List:{}".format(listA))
else:
    listA.insert(int(position)-1,data)
    print("List after adding {} Element at position {} is: {}".format(data,position,listA))




