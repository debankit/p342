import deb_lib

def function(x):
    return 4 / ( 1 + x**2)

#defining the variables required
maxn = 100000
nvalues = []
fnvalues = []
sigmavalues = []

#Loop for calculating the pi value and error in each iteration
for i in range(10 , maxn, 50):
    nvalues.append(i)
    fn, sigma = deb_lib.monteCarlo_Integration(function, 0, 1, i)
    fnvalues.append(fn)
    sigmavalues.append(sigma)

#Exporting the output to a text file
j = open("6q3.txt", 'a')
for i in range(len(nvalues)):
    j.write("%i                %5.21f               %5.21f\n" % (nvalues[i], fnvalues[i], sigmavalues[i]))
j.close()

#Printing the last result
print("final values\n")
print(nvalues[-1],"     ", fnvalues[-1],"           ", sigmavalues[-1])

#Output
#final values

#99960       3.141015322031225             0.6417589461087645