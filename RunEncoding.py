# 	Run Length Encoding list

Sample_list = ['A', 'B', 'a', 'a','r','a','a', 'a', 'i', 'i', 'i', 'i', 'z']
New_list = []
Temp_list = []
temp = Sample_list[0]
count=1
for i in Sample_list:
    if i == temp:
        count += 1
    else:
        Temp_list.append(count)
        Temp_list.append(temp)
        New_list.append(Temp_list[:])
        Temp_list.clear()
        temp = i
        count = 1
print(New_list)

