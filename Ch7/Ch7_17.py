scores={'Ch':100,'En':80, 'Ma':95, 'Na': 90}

v1 =  scores.pop('Ma')
print(v1)
print(scores)
v2 =  scores.pop('EE',"Empty")#可給預設值
print(v2)
print(scores)
del scores["En"]
print(scores)
