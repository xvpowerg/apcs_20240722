poem = '''床前明月光
疑是地上霜
舉頭望明月
低頭思故鄉
'''
try:
    print(poem,file = open("output.txt","w"),flush=True)     
except Exception as ex:
    print("寫出失敗:",ex)    
