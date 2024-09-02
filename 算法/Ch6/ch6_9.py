import itertools
list_1to9 = [1,2,3,4,5,6,7,8,9]
prem_list = list(itertools.permutations(list_1to9))
def toNumber(data):
    ans = 0
    offset = 0
    for i in range(3):
        ans +=  data[0 + offset]/(data[1+ offset]*10+data[2+ offset])
        offset+= 3
    return ans
    
for i in prem_list:
    if toNumber(i) == 1:
        print(f"{i[0]}     {i[3]}      {i[6]}")
        print(f"{i[1]}{i[2]}  {i[4]}{i[5]}   {i[7]}{i[8]}")
        print()
