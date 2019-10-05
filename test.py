import time
start =time.perf_counter()
i=0
for i in range(30000000):
    print(i+i)
end = time.perf_counter()
print('Running time: %s Seconds'%(end-start))


print("ok")
