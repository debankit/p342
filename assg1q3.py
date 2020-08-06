# Sum over 1+ 1/2 + 1/3 + ..... till 1/1000

num = 1
sum = 0.0
while(num < 1000):
       sum += (1.0/num)
       num += 1
print("The sum is", sum)
