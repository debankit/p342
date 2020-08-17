#to find the average distance between points 2-d grid containing 36 points
sum=0
n=36
total= n*n
for xi in range(6):
    for yi in range(6):
        for xf in range(6):
            for yf in range(6):
                        sum= sum + abs(xi-xf) + abs(yi-yf)
print("Average distance between two points = ", sum/total)
