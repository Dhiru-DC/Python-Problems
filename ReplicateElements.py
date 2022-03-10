# Replicate Elemments in a list

def ReplicateList(List,Factor):
    Output_List=[x for x in List for i in range(Factor)]
    return Output_List

Sample_list = ['A','B','C']
Factor = int(input("How Many times to repeat?"))
print(ReplicateList(Sample_list,Factor))


