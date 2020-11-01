import deb_lib

def function(x):
    return (x / (1 + x))

#Comparing the different method for numerical integration in tabular form
print("For 6 iterations: \n")
print("Midpoint Method:",deb_lib.midpoint_Integration(function, 1, 3, 6) ,"    Trapezoidal Method:",deb_lib.trapezoidal_Integration(function, 1, 3, 6) ,"    Simpson Method:", deb_lib.simpson_Integration(function, 1, 3, 6))
print(" ")
print("For 10 iterations: \n")
print("Midpoint Method:",deb_lib.midpoint_Integration(function, 1, 3, 10) ,"    Trapezoidal Method:",deb_lib.trapezoidal_Integration(function, 1, 3, 10) ,"    Simpson Method:", deb_lib.simpson_Integration(function, 1, 3, 10))
print(" ")
print("For 26 iterations: \n")
print("Midpoint Method:",deb_lib.midpoint_Integration(function, 1, 3, 26) ,"    Trapezoidal Method:",deb_lib.trapezoidal_Integration(function, 1, 3, 26) ,"    Simpson Method:", deb_lib.simpson_Integration(function, 1, 3, 26))

#Output
#For 6 iterations:

#Midpoint Method: 1.3077156791250208    Trapezoidal Method: 1.3051226551226551      Simpson Method: 1.3068302068302067

#For 10 iterations:

#Midpoint Method: 1.3071646395900398    Trapezoidal Method: 1.3062285968245722      Simpson Method: 1.3068497693110694

#For 26 iterations:

#Midpoint Method: 1.3068990323038625    Trapezoidal Method: 1.3067603809022117      Simpson Method: 1.3068527513069688