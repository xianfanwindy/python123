#w3e1
dayup = 1
def dayUp(df):
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1+df)
        else:
            dayup = dayup*(1-0.09)
