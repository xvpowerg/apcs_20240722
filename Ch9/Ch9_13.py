import time
print(time.time())
print(time.ctime())
lt = time.localtime()
print(lt.tm_year,lt.tm_mon,lt.tm_mday)

print(time.ctime())
time.sleep(2)
print(time.ctime())
time.sleep(2)
print(time.ctime())
