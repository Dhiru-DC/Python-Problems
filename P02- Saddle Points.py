#P02 - Easy Problems Saddle Points

saddle_points = [[34, 21,32, 41, 25],[14,42,43,44,31],[54,45,52,42,23],[33,15,51,47,35],[21,52,33,48,23]] #Input Array

#List containing maximum value per row


#To convert row into columns and vice versa

inverse_saddle_points = [[row[i] for row in saddle_points] for i in range(5)]

#Finding minimum per column

min_per_column=[min(i) for i in inverse_saddle_points]

count=0

#To get the index of each element which is maximum per row and checking if it is the minmum in that column as well
for i in saddle_points:
    k=0
    m=0
    for j in i:
        if j>=max(i) and j <=min_per_column[k]:
            print(m,k)
            count+=1
        m += 1
        k += 1
if count==0:
    print("None")
