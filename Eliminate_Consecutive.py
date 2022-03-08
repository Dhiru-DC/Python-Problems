# 	Eliminate Consecutive Repeated Elements in a list

Sample_list = ['A', 'B', 'a', 'a', 'e', 'r', 'a','i', 'i', 'i', 'i', 'z']
Final_list =[]
temp=''
for i in Sample_list:
    if i != temp:
        Final_list.append(i)
        temp = i
print(Final_list)


