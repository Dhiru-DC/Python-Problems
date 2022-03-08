sample_list = [1,2,3,4,[5,6,6,5,8,9,0],23,45,6,77,8,[89,11]]

Final_list=[]
for i in sample_list:
	if isinstance(i,int)==True:
		Final_list.append(i)
	else:
		for x in i:
			Final_list.append(x)

print("Flattened list is:" + str(Final_list))
