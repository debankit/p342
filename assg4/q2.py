import matrixlib

#Question2
a = []
matrixlib.read('q2mat.txt', a)

o = []
matrixlib.read('q2mat.txt', o)

b = []
matrixlib.read('q2id.txt',b)

#Pivoting the Augmented Matrix
c = matrixlib.partial_pivot(a, b)

#LU decomposition
matrixlib.lu_dec(a)

#Finding the determinant
p = matrixlib.det_upper(a)
if(c%2 == 0):
    print("Determinant is :" , p)
else:
    print("Determinant is :", -1 * p )

if(p != 0):
    print("Inverse exists as determinant is non zero")
    # Executing Forward Backward Substitution
    x = matrixlib.forback_sub(a, b)
    # Printing the Solution
    print("Solution of Question 2:")
    matrixlib.write(x)
    # Checking the Inverse
    print("Checking the Inverse:")
    matrixlib.write(matrixlib.mat_multi(o, x))

else:
    print("Inverse doesn't exists as determinant is 0")

#Output
#Determinant is : -36.0
#Inverse exists as determinant is non zero
#Solution of Question 2:
#[-0.25000000000000006, 1.6666666666666672, -1.8333333333333333, 0.3333333333333333]
#[0.08333333333333337, -0.666666666666667, 0.8333333333333333, 0.0]
#[0.16666666666666666, -0.33333333333333326, -0.3333333333333333, 0.0]
#[-0.08333333333333333, 0.6666666666666666, 0.16666666666666666, 0.0]
#hecking the Inverse:
#[1.0, 0.0, 0.0, 0.0]
#[0.0, 1.0, 0.0, 0.0]
#[4.163336342344337e-17, -3.3306690738754696e-16, 0.9999999999999999, 0.0]
#[2.7755575615628914e-17, -2.220446049250313e-16, -2.7755575615628914e-16, 1.0]
