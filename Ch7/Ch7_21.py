def testScore(score):
    if score <0 or score > 100:
        #print("錯誤的成績")
        #return -1
        raise Exception("錯誤的成績")
    else:
         return score
    #score < 0 or score > 100 就是錯
    #如果錯顯示錯的成績 回傳-1
    #如果正確回傳成績

print("開始")   
s1 = testScore(-10)
print(s1)
print("完成")   
    
