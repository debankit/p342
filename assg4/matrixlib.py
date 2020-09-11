#Reading a Matrix from a file
def read(fil , A):
    file = open(fil , 'r')
    for line in file:
        ns = line.split()
        no = [float(n) for n in ns]
        A.append(no)
    file.close()

#To print the Matrix
def write(x):
    for r in range(len(x)):
        print(x[r])

#Function for partial pivoting the Augmented Matrix / Only Matrix
def partial_pivot(a, b):
    n= len(a)
    counter = 0
    for r in range(0 , n):
        if abs(a[r][r]) == 0:
            for r1 in range(r+1 , n):
                if abs(a[r1][r]) > abs(a[r][r]):
                    counter = counter + 1
                    for x in range(0,n):
                        d1= a[r][x]
                        a[r][x] = a[r1][x]
                        a[r1][x] = d1
                    if(b!= 0):
                         d1 = b[r]
                         b[r] = b[r1]
                         b[r1] = d1
    return counter


#Multiplication of Matrices
def mat_multi(a, b):
    m = len(b[0])
    l=len(b)
    n = len(a)
    p2 = [[0 for y in range(m)] for x in range(n)]
    for x in range(n):
        for i in range(m):
            for y in range(l):
                p2[x][i] = p2[x][i] + (a[x][y] * b[y][i])
    return p2


# Forward- Backward Substitution
def forback_sub(a, b):
    m = len(b[0])
    n = len(a)
    # forward substitution
    y = [[0 for y in range(m)] for x in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(i):
                s = s + a[i][k] * y[k][j]
            y[i][j] = b[i][j] - s
    # backward substitution
    x = [[0 for y in range(m)] for x in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            s = 0
            for k in range(i + 1, n):
                s = s + a[i][k] * x[k][j]
            x[i][j] = (y[i][j] - s) / a[i][i]

    return x

#L-U decomposition
def lu_dec(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            s = 0
            if(i<=j):
                for k in range(i):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = a[i][j] - s
            else:
                for k in range(j):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = (a[i][j] - s) / a[j][j]

#Finding determinant of Upper Triangular Matrix
def det_upper(a):
    n = len(a)
    p = 1
    for i in range(n-2):
        p = p * a[i][i]
    p = p * (a[n-2][n-2] * a[n-1][n-1])
    return p
