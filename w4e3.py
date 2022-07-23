#intadd.py
sum=0
symbol=1
for i in range(1,966+1):
    sum=sum+i*symbol
    symbol*=-1
print(sum)
