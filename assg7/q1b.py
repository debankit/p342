import math
import deb_lib

def func1(y, x):
    return 6 - ((2*y) / x)

x = []
y = []

#initial values
x.append(3)
y.append(1)

deb_lib.explicit_Euler(func1, x , y, 60)

j = open("q1b.txt", 'a')
for i in range(len(x)):
    j.write("%5.21f                %5.21f\n" % (x[i] , y[i]))
j.close()

print("For Q1.(b) solution at x = %.0f is %s" % (x[-1], str(y[-1])))

#Output
#For Q1.(b) solution at x = 60 is 120.59095477386926
