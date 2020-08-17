#to find the average distance between points in a straight line containing 6 points
sum=0
n=6
total= n*n
for x in range(n):
    for y in range(n):
        sum= sum + abs(x-y)
print("Average distance between two points = ", sum/total)
#Average distance between two points =  1.9444444444444444
