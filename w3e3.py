base = 1.0
factor = 0.01
a = pow(base+factor,365)
b = 1.0
while b < a:
    b=1.0
    for i in range(365):
        if i % 7 in [6,0]:
            b=b*(base-0.01)
        else:
            b=b*(base+factor)
    factor = factor + 0.001
print("工作日的努力参数是: {:.3f}".format(factor-0.001))
