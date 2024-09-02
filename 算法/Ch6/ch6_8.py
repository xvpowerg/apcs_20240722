import itertools
list_1to9 = [1,2,3,4,5,6,7,8,9]
prem_list = list(itertools.permutations(list_1to9))
def toNumber(data):
    return data[0]/(data[1]*10+data[2]) + data[3]/(data[4]*10+data[5]) + data[6]/(data[7]*10+data[8])
    
for i in prem_list:
    if toNumber(i) == 1:
        print(f"{i[0]}     {i[3]}      {i[6]}")
        print(f"{i[1]}{i[2]}  {i[4]}{i[5]}   {i[7]}{i[8]}")
        print()
