import deb_lib
import math

def function(x):
    return (math.exp(-x**2))

#Finding the upper bound of N from the given error for different methods
def midpoint_limit(a, b, mn , f2ndmax):
    return math.ceil(math.sqrt( ((math.pow(b-a, 3)) * f2ndmax) / (24 * mn) ) )

def trapezoidal_limit(a, b, tn , f2ndmax):
    return math.ceil( math.sqrt( ((math.pow(b-a, 3)) * f2ndmax) / (12 * tn) ) )

def simpsom_limit(a, b, sn , f4thmax):
    if(math.ceil(math.pow( (((math.pow(b-a, 5)) * f4thmax) / (180 * sn)) , (1/4) )) % 2 == 0):
        return math.ceil(math.pow( (((math.pow(b-a, 5)) * f4thmax) / (180 * sn)) , (1/4) ))
    else:
        return (math.ceil(math.pow( (((math.pow(b-a, 5)) * f4thmax) / (180 * sn)) , (1/4) )) + 1)

#Calculating and printing the integration using different methods
print("Midpoint method", deb_lib.midpoint_Integration(function, 0, 1, midpoint_limit(0 , 1, 0.001, 2 )))
print("Trapezoidal method", deb_lib.trapezoidal_Integration(function, 0, 1, trapezoidal_limit(0, 1, 0.001, 2 )))
print("Simpson method", deb_lib.simpson_Integration(function, 0, 1, simpsom_limit(0, 1, 0.001, 12)))

#Output
#Midpoint method 0.7471308777479975
#Trapezoidal method 0.7464612610366896
#Simpson method 0.7468553797909873