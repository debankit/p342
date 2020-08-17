#to find the average distance between points in a straight line containing 6 points
sum=0
n=6
total= n*n
for x in range(6):
    for y in range(6):
        sum= sum + abs(x-y)
print("Average distance between two points = ", sum/total)
