# Reading two matrices and printing their products
with open('m.txt', 'r') as f:
    m = [[int(num) for num in line.split()] for line in f]

with open('n.txt', 'r') as j:
    n = [[int(num) for num in line.split()] for line in j]

a= [1, 2, 3]
p1=[0, 0, 0]
p2=[[0,0,0], [0,0,0], [0,0,0]]
for x in range(3):
        for y in range(3):
            p1[x] = p1[x] + (m[x][y] * a[y])
print("Product of M*A: ",p1)
for x in range(3):
    for i in range(3):
        for y in range(3):
            p2[x][i] = p2[x][i] + (m[x][y] * n[y][i]) 
print("Product of M*N: ", p2)



#Output
#Product of M*A:  [50, 32, 22]
#Product of M*N:  [[64, 338, 231], [88, 95, 102], [68, 43, 45]]
# M= 3 22 1         N= 3 2 1
#    4 5 6             2 15 10
#    11 1 3            11 2 8
