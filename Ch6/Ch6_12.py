def personInfo(name,age,**other):
    print("=====info=====")
    print("name:",name)
    print("age:",age)
    for key in other:
        print(key,":",other[key])
personInfo("Vivin",20)
personInfo("Lucy",18,phone="098054321",compay="IBM")
