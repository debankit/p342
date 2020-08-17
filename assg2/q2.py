#to define two matrices and find their sum and dot product
a = [2, 5, 7]
b = [6, 6, 8]
sum = []
dot = 0
for x in range(3):
    sum.append( a[x]+b[x] )
for x in range(3):
    dot= dot+ (a[x]*b[x] )
print("Sum of the matrices")
for x in sum:
    print(x)
print("Dot prodduct of the Matrices")
print(dot)
