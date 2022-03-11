#Remove Kth Element from the list

listA = ['a', 'e', 'i', 'o', 'u','c', 'd', 'f']
Element=int(input("Enter the Index of element to be removed:"))
if Element>len(listA):
    print("Invalid index")
    print("Failed to remove Element, List:{}".format(listA))
else:
    listA.pop(Element-1)
    print("List after removing {} Element is: {}".format(Element,listA))




