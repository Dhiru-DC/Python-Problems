#Print Random numbers from list
import random as r

listA = ['a', 'e', 'i', 'o', 'u','c', 'd', 'f']
Total_Numbers=int(input("How many random elements to be chosen from the list?:"))
if(Total_Numbers>len(listA) or Total_Numbers < 1):
    print("Not Allowed")
else:
    listB= r.sample(listA,Total_Numbers)
    print(listB)
