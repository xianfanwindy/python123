import random
random.seed(123)
dit=0
n=eval(input())
for i in range(1,n+1):
    x=random.random()
    y=random.random()
    if pow(x**2+y**2,1/2) <=1:
        dit+=1
pi=dit/n*4
print("{:6f}".format(pi))
