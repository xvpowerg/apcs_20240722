def func():
    global a
    a += 2
    print("func() a= ",a)
    
a = 5
print("全域:a=",a)
func()
print("全域:a=",a)
