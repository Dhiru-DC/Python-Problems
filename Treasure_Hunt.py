# Easy Problem P01 - Treasure Hunt

treasure_hunt = [[34, 21,32, 41, 25],[14,42,43,14,31],[54,45,52,42,23],[33,15,51,31,35],[21,52,33,13,13,23]] # 5 by 5 Array

row,column=(0,0)
final_set=set()
final_set.add(treasure_hunt[row][column])
cell=row*10 + column
while cell not in final_set: #to check if that cell was already visited if yes then exit the loop to avoid infinite loop
    
    print(treasure_hunt[row][column],end=" ")
    row_1=treasure_hunt[row][column]//10
    column_1=treasure_hunt[row][column]%10
    if row!=0 and column!=0:
        final_set.add(cell)
        cell = row_1*10 + column_1
    row =row_1 -1
    column =column_1 - 1


