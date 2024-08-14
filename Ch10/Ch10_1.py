filename = input("請輸入讀取檔名:")

try:    
  fin = open(filename)
  line = fin.readline()
  print(line)
  while line:
    print(line,end="")
    line = fin.readline()
except FileNotFoundError:
    print("錯誤的檔名")
finally:
    try:        
        fin.close()
    except:
        pass
