# Duplicate Elemments in a list

Sample_list = ['A', 'B', 'C', 'D', 'E']
i = 0
j=len(Sample_list)
while i < (2*j):
    Sample_list.insert(i + 1, Sample_list[i])
    i += 2
print(Sample_list)

