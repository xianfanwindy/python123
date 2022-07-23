#w1e5

TempStr = input()

if TempStr[:3] == "RMB":
    usd = eval(TempStr[3:])/6.78
    print("USD{:.2f}".format(usd))
elif TempStr[:3] in ["USD"]:
    rmd = eval(TempStr[3:])*6.78
    print("RMB{:.2f}".format(rmd))
else:
    print() #不提示输出格式错误
