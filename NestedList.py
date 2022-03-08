sample_list = [1,2,3,4,[5,6,[6,[5]],8,9,0],23,45,6,77,8,[89,11]]
Final_list=[]

def FlattenedList(NestedList):
    for i in NestedList:
        if isinstance(i, int):
            Final_list.append(i)
        else:
            FlattenedList(i)
    return 1


FlattenedList(sample_list)
print("Flattened list is:" + str(Final_list))
