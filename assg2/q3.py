# Reading two matrices and printing their products
with open('m.txt', 'r') as f:
    m = [[int(num) for num in line.split()] for line in f]

with open('n.txt', 'r') as f:
    n = [[int(num) for num in line.split()] for line in f]

a= [[1, 1, 2], [1, 1, 1], [1, 1, 3]]
p1=[[0,0,0], [0,0,0], [0,0,0]]
p2=[[0,0,0], [0,0,0], [0,0,0]]
for x in range(3):
    for i in range(3):
        for y in range(3):
            p1[x][i] = p1[x][i] + (m[x][y] * a[y][i])
print("Product of M*A: ",p1)
for x in range(3):
    for i in range(3):
        for y in range(3):
            p2[x][i] = p1[x][i] + (m[x][y] * n[y][i]) 
print("Product of M*N: ", p2)
#Product of M*A:  [[26, 26, 31], [15, 15, 31], [15, 15, 32]]
#Product of M*N:  [[37, 28, 39], [81, 27, 79], [48, 21, 56]]
