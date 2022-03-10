# Decompress List

Sample_list = [[4, 'A'], 'B', [2, 'C'], [3, 'i'],'Z']
Output_list = []
for i in Sample_list:
    if isinstance(i, list):
        x = i[0]
        for k in range(x):
            Output_list.append(i[1])
    else:
        Output_list.append(i)
print(Output_list)

