for a in range(1,10):
    for b in range(10):
        for c in range(10):
            n=a*100+b*10+c
            if a**3+b**3+c**3==n:
                print("{}".format(n),end=',')
