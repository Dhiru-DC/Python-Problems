# Print range of list between numbers

a,b=(input("Enter the range for list:").split())
a=int(a)
b=int(b)
if a>b:
    Output_list=list(range(b,a+1))
    print("Following is the list between {} and {}:{}".format(b,a,Output_list))
else:
    Output_list = list(range(a,b+1))
    print("Following is the list between {} and {}:{}".format(a,b,Output_list))
