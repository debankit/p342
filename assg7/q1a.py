import math
import deb_lib

def func1(y, x):
    return (y * math.log(y)) / x

x = []
y = []

#initial values
x.append(2)
y.append(2.71828)

deb_lib.explicit_Euler(func1, x , y , 60)

j = open("q1a.txt", 'a')
for i in range(len(x)):
    j.write("%5.21f                %5.21f\n" % (x[i] , y[i]))
j.close()

print("For Q1.(a) solution at x = %.0f is %s" % (x[-1], y[-1]))

#Output
#For Q1.(a) solution at x = 60 is 42300784541.69497
