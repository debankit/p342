import matrixlib

#Question1
a = []
matrixlib.read('q1a.txt', a)

b = []
matrixlib.read('q1b.txt',b)

#Pivoting the Augmented Matrix
c = matrixlib.partial_pivot(a, b)

#LU decomposition
matrixlib.lu_dec(a)

#Executing Forward Backward Substitution
x = matrixlib.forback_sub(a,b)

#Printing the Solution
print("Solution of Question 1:")
matrixlib.write(x)


#Output
#Solution of Question 1:
#[1.0]
#[-1.0]
#[1.0]
#[2.0]