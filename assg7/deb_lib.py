import math , random

"""---------------------------------------------------------------------------------------"""
#Reading a Matrix from a file
def read_Matrix(fil , A):
    file = open(fil , 'r')
    for line in file:
        ns = line.split()
        no = [float(n) for n in ns]
        A.append(no)
    file.close()

"""---------------------------------------------------------------------------------------"""
#To print the Matrix
def write_Matrix(x):
    for r in range(len(x)):
        print(x[r])

"""---------------------------------------------------------------------------------------"""
#Factorial Method
def factorial(num):
    fact = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            fact = fact * i
        return fact

"""---------------------------------------------------------------------------------------"""
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

"""---------------------------------------------------------------------------------------"""
#Multiplication of Matrices
def matrix_Multiplication(a, b):
    m = len(b[0])
    l=len(b)
    n = len(a)
    p2 = [[0 for y in range(m)] for x in range(n)]
    for x in range(n):
        for i in range(m):
            for y in range(l):
                p2[x][i] = p2[x][i] + (a[x][y] * b[y][i])
    return p2

"""---------------------------------------------------------------------------------------"""
#Gauss-Jordan Method
def gauss_Jordan(a , b):
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

"""---------------------------------------------------------------------------------------"""
# Forward- Backward Substitution
def forwardbackward_Substitution(a, b):
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

"""---------------------------------------------------------------------------------------"""
#L-U decomposition
def lu_Decomposition(a):
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

"""---------------------------------------------------------------------------------------"""
#Finding determinant of Upper Triangular Matrix
def uppertriangular_Determinant(a):
    n = len(a)
    p = 1
    for i in range(n-2):
        p = p * a[i][i]
    p = p * (a[n-2][n-2] * a[n-1][n-1])
    return p

"""---------------------------------------------------------------------------------------"""
#Bracketing the root
def bracket_Root(f , a):
    fa = f(a[0])
    fb = f(a[1])
    beta = 0.7
    for i in range(12):
        if ((fa * fb) < 0):
            return True
        if((fa * fb) > 0):
            if(abs(fa) < abs(fb)):
                a[0] = a[0] - beta * (a[1] - a[0])
            elif(abs(fa) > abs(fb)):
                a[1] = a[1] + beta * (a[1] - a[0])
    if ((fa * fb) < 0):
        return True
    else:
        return False

"""---------------------------------------------------------------------------------------"""
#Bisection method for root, where f is function and a are guess values
def bisection_Root(f , a):
    epsilon = pow(10, -6)
    if (bracket_Root(f, a)):
        for i in range(200):
            c = (a[0] + a[1]) / 2
            if ((f(a[0]) * f(c)) < 0):
                a[1] = c
            elif ((f(a[0]) * f(c)) > 0):
                a[0] = c
            elif((f(a[0]) * f(c)) == 0):
                if(abs(f(c)) == 0):
                    print("The root is", c)
                    return True
                elif(abs(f(a[0])) == 0):
                    print("The root is", a[0])
                    return True
            j = open("q1bbisectionfile.txt", 'a')
            j.write("%i         %5.21f\n" % (i+1, abs(a[1]-a[0])) )
            j.close()
            if (abs(a[1] - a[0]) < epsilon):
                return True
    else:
        print("Very bad guess for bracketing")
        return False

"""---------------------------------------------------------------------------------------"""
#False Position method for root, where f is function and a are guess values
def regularfalsi_Root(f , a):
    epsilon = pow(10, -6)
    z = 0
    if (bracket_Root(f, a)):
        for i in range(200):
            if( i != 0):
                z = c
            c = a[1] - ( ((a[1] - a[0]) * f(a[1])) / (f(a[1]) - f(a[0]) ))
            if ((f(a[0]) * f(c)) < 0):
                a[1] = c
            elif ((f(a[0]) * f(c)) > 0):
                a[0] = c
            elif((f(a[0]) * f(c)) == 0):
                if(abs(f(c)) == 0):
                    print("The root is", c)
                    return True
                elif(abs(f(a[0])) == 0):
                    print("The root is", a[0])
                    return True
            j = open("q1bregularfalsifile.txt", 'a')
            j.write("%i         %5.21f\n" % (i+1, abs(z - c)))
            j.close()
            if(i != 0):
                if (abs(z - c) < epsilon):
                    a[1] = c
                    return True
    else:
        print("Very bad guess for bracketing")
        return False

"""---------------------------------------------------------------------------------------"""
#Finding first derivative
def first_Derivative(f , x):
    h = math.pow(10 , -4)
    return ((f(x + h) - f(x - h)) / (2 * h))

"""---------------------------------------------------------------------------------------"""
#Newton Raphson
def newtonraphson_Root(f , x):
    x1 = x
    epsilon = pow(10 , -6)
    for i in range(200):
        n = f(x1)
        m = first_Derivative(f, x1)
        x1 = x1 - (n / m)
        j = open("q1bnewtonraphsonfile.txt", 'a')
        j.write("%i         %5.21f\n" % (i + 1, abs(x1 - x)))
        j.close()
        if (abs(x1 - x) < epsilon):
            return x1
        x = x1

"""---------------------------------------------------------------------------------------"""
#Finding the First Derivative of polynomial, where p is polynomial method, c is coefficient array, i is the step of synthetic division, x is the value
def polynomialfirst_Derivative(p, c, i, x):
    h = math.pow(10, -6 )
    return ((p(c, i, (x+h) ) - p(c, i, (x-h) )) / (2 * h))

"""---------------------------------------------------------------------------------------"""
#Finding second derivative of polynomial, where p is polynomial method, c is coefficient array, i is the step of synthetic division, x is the value
def polynomialsecond_Derivative(p , c, i, x):
    h = math.pow(10, -6)
    m = polynomialfirst_Derivative(p, c, i, x + h)
    n = polynomialfirst_Derivative(p, c, i, x - h)
    return ((m - n) / (2 * h))

"""---------------------------------------------------------------------------------------"""
# Synthetic Division Method for Deflation of Polynomials, where p is polynomial method, c is coefficient array, a0 is the guess value, r is solution array
def synthetic_Division(p, c, a0, r):
    for i in range(len(c) - 2):
        x1 = laguerre_Method(p, c, i, a0)
        for j in range(3 - i):
            c[j+1] = c[j+1] + (x1 * c[j])
        c[len(c) -1 - i] = 0
        r.append(x1)

"""---------------------------------------------------------------------------------------"""
#Laguerre Method for roots of polynomial, where p is polynomial method, c is coefficient array, i is the step of synthetic division, a0 is the guess value
def laguerre_Method(p, c, i, a0):
    e = len(c) - 1
    epsilon = math.pow(10, -4)
    if(p(c, i, a0) == 0):
        return a0
    else:
        for j in range(100):
            g = (polynomialfirst_Derivative(p, c, i, a0)) / p(c, i, a0)
            h = (math.pow(g, 2)) - ((polynomialsecond_Derivative(p, c, i, a0)) / p(c, i, a0))
            d1 = (g + math.sqrt(abs((e-i-1)*(( (e-i) * h ) - math.pow(g, 2)))))
            d2 = (g - math.sqrt(abs((e-i-1)*(( (e-i) * h) - math.pow(g, 2)))))
            if(abs(d1) > abs(d2)):
                a = (e-i) / d1
            else:
                a = (e-i) / d2
            a1 = a0 - a
            if(abs(a1 - a0) < epsilon):
                return a0
            a0 = a1




"""---------------------------------------------------------------------------------------"""
"Integration"

#Finding the integral value using midpoint method
def midpoint_Integration(f , a , b , n):
    h = (b - a) / n
    sum = 0
    for i in range(n):
        sum += h * f( ((a + (i * h)) + (a + ((i + 1) * h))) / 2)
    return sum

"""---------------------------------------------------------------------------------------"""
#Finding the integral value using trapezoidal method
def trapezoidal_Integration(f, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(1 , n+1):
        sum += (h / 2) * (f(a + ((i - 1) * h) ) + f(a + (i * h)) )
    return  sum

"""---------------------------------------------------------------------------------------"""
#Finding the integral value using simpson method
def simpson_Integration(f, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(2 , n+1 , 2):
        sum += ( h /3 ) * (f(a + ((i - 2) * h)) + 4 * f(a + (( i - 1) * h)) + f( a + (i * h)) )
    return sum

"""---------------------------------------------------------------------------------------"""

#Monte Carlo Method for estimating the integrals
def monteCarlo_Integration(f, a, b, n):
    randomnumber = 0
    sumf = 0
    sumsigma2= 0
    fn = 0
    sigma = 0
    for i in range(n):
        randomnumber = random.random()
        sumf += f(a+(b-a)*randomnumber)
        sumsigma2 += f(a+(b-a)*randomnumber) ** 2
    sigma = math.sqrt((sumsigma2/n) - ((sumf / n) ** 2))
    fn = ((b - a) * sumf) / n
    return fn, sigma
"""---------------------------------------------------------------------------------------"""
"""---------------------------------------------------------------------------------------"""


#Euler's Forward / Explicit Method
def explicit_Euler(func1, x, y, xlimit):
    h = 0.3
    i = 0
    while(x[i] < xlimit):
        i = i + 1
        x.append(x[i-1] + h)
        y.append(y[i-1] + h * func1(y[i-1] , x[i-1]))

"""---------------------------------------------------------------------------------------"""

#Runge-Kutta Method for 2nd order differential equation
def runge_kuttaR4(fy, fz, x, y, z, xlimit, h, txt_file):
    file = open(txt_file, "w")
    while(x < xlimit):
        file.write("%5.21f                %5.21f                %5.21f\n" % (x, y, z))
        k1y = h * fy(z, x)
        k1z = h * fz(y, z, x)

        k2y = h * fy(z + (k1z / 2), x + (h / 2))
        k2z = h * fz(y + (k1y / 2), z, x + (h / 2))

        k3y = h * fy(z + (k2z / 2), x + (h / 2))
        k3z = h * fz(y + (k2y / 2), z, x + (h / 2))

        k4y = h * fy(z + k3z, x + h)
        k4z = h * fz(y + k3y, z, x + h)

        y = y + (1 / 6) * (k1y + 2 * k2y + 2 * k3y + k4y)
        z = z + (1 / 6) * (k1z + 2 * k2z + 2 * k3z + k4z)
        x = x + h
    file.write("%f  %lf %lf\n" % (x, y, z))
    file.close()
    return y, xlimit

"""---------------------------------------------------------------------------------------"""

#Shooting Method
def ode_ShootingMethod(fy, fz, x, xlimit, y, yn, zl, zh, h, txt_file):
    z0 = zl
    for i in range(50):
        txt_filel = "%s_l%i.txt" % (txt_file,i)
        y_el, xl = runge_kuttaR4(fy, fz, x, y, z0 ,xlimit,h,  txt_filel)
        if abs(y_el - yn) < 10 ** (-6):
            return y_el,z0
        else:
            txt_fileh = "%s_h%i.txt" % (txt_file,i)
            z0 = zh
            y_eh, xh = runge_kuttaR4(fy, fz, x, y, z0,xlimit, h, txt_fileh)
            if abs(y_eh - yn) < 10 ** (-6):
                return y_eh,z0
            elif y_el < yn and yn < y_eh:
                z0 = zl + (zh - zl) * (yn - y_el) / (y_eh - y_el)
            elif y_eh < yn and yn < y_el:
                z0 = zh + (zl - zh) * (yn - y_eh) / (y_el - y_eh)
            else:
                print("Chosse differnt values of z(%.0f)"%(x))
                return None,None