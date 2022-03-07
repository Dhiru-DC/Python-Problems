import sys

Sample_list = ['A','B','a','v','e','r',100,20,14]
a=int(sys.argv[1]) - 1
if a > len(Sample_list) - 1 or a < 0:
  print("Out of Bound")
else:
  print(str(a) + 'th element is:' + Sample_list[a])
