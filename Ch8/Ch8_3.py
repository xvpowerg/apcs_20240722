try:
    for i in range(1,5):
        for k in range(1,5):
            if i == 3:
                raise Exception()
            print(i,"_",k,end= " ")
        print()    
except:
    pass#因為不打字會出錯 又沒事要做所以加pass
