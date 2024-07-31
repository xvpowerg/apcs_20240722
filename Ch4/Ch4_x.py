dict1 = {"a":100,"b":200,"c":300}
print(dict1)
dict2 = {"a":200,"b":400}
print(dict2)
dict3 = {"a":[1,2,3],"b":[22,23,24,25]}

print(dict1["a"])
print(dict2["b"])
#print(dict1["x"])#KeyError: 'x'

dict2["b"] = 75
print(dict2["b"])
dict2["y"] = 88
print(dict2["y"])
print(dict3["a"][:2])
dict3["a"].append(7)
print(dict3["a"])
