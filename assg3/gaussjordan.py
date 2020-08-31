
def partial_pivot(a, b):
    n= len(a)
    for r in range(0 , n):
        if abs(a[r][r]) == 0:
            for r1 in range(r+1 , n):
                if abs(a[r1][r]) > abs(a[r][r]):
                    for x in range(0,n):
                        d1= a[r][x]
                        a[r][x] = a[r1][x]
                        a[r1][x] = d1
                        d1 = b[r]
                        b[r] = b[r1]
                        b[r1] = d1

def gauss_jordan(a , b):
    n = len(a)
    bn = len(b[0])
    for r in range(0 , n):
        partial_pivot(a , b)
        pivot = a[r][r]
        for c in range(r , n):
            a[r][c] = a[r][c]/pivot
        for c in range(0 , bn):
            b[r][c] = b[r][c]/pivot
        for r1 in range(0, n):
            if r1==r or a[r1][r] == 0:
                continue
            else:
                factor = a[r1][r]
                for c in range(r , n):
                    a[r1][c] = a[r1][c] - factor*a[r][c]
                for c in range(0 , bn):
                    b[r1][c] = b[r1][c] - factor*b[r][c]

def mat_multi(a , b):
    p2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    n = len(a)
    for x in range(n):
        for i in range(n):
            for y in range(n):
                p2[x][i] = p2[x][i] + (a[x][y] * b[y][i])
    print("Product of matrices to check the inverse ")
    for r in p2:
        print(r)


with open('q1a.txt', 'r') as f:
    m1 = [[int(num) for num in line.split()] for line in f]

with open('q1b.txt', 'r') as f:
    b1 = [[int(num) for num in line.split()] for line in f]

gauss_jordan(m1 , b1)
print("Solution for 1st question: ")
for x in range(0 , 3):
    print(b1[x][0])

with open('q2a.txt', 'r') as f:
    m2 = [[int(num) for num in line.split()] for line in f]

with open('q2b.txt', 'r') as f:
    b2 = [[int(num) for num in line.split()] for line in f]

gauss_jordan(m2 , b2)
print("Solution for 2nd question: ")
for x in range(0 , 3):
    print(b2[x][0])

with open('a.txt', 'r') as f:
    a = [[int(num) for num in line.split()] for line in f]

with open('id.txt', 'r') as f:
    id = [[int(num) for num in line.split()] for line in f]


gauss_jordan(a , id)
print("Inverse of the given matrix:")
for r in id:
    print(r)

with open('a.txt', 'r') as f:
    ac = [[int(num) for num in line.split()] for line in f]

mat_multi(ac , id)


#Output
#Solution for 1st question:
#3.0
#1.0
#-2.0
#Solution for 2nd question:
#-2.0
#-2.0
#1.0
#Inverse of the given matrix:
#[-3.0, 3.0, -7.0]
#[1.0, 1.0, 0.0]
#[1.0, 0.0, 1.0]
#Product of matrices to check the inverse
#[1.0, 0.0, 0.0]
#[0.0, 1.0, 0.0]
#[0.0, 0.0, 1.0]
