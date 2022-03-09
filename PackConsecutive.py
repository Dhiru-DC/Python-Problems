# 	Pack Consecutive Repeated Elements in a list

Sample_list = ['A', 'B', 'a', 'a', 'e', 'r', 'a', 'i', 'i', 'i', 'i', 'z']
New_list = []
Temp_list = []
temp = Sample_list[0]
for i in Sample_list:
    if i == temp:
        Temp_list.append(i)
    else:
        New_list.append(Temp_list[:])
        Temp_list.clear()
        Temp_list.append(i)
        temp = i
print(New_list)

