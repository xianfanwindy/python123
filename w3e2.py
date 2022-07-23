import time
start = time.perf_counter()
time.sleep(0.2)
end = time.perf_counter()
dur = end - start
#print("{:-^}".format("执行开始"))
print("执行开始".center(20,'-'))
print("{:.2f}s".format(dur))
