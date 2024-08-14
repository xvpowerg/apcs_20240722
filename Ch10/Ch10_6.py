try:
   file = open("data2.csv","r")
   line = file.readline()
   while line:
       #print(line,end=" ")
       dataList =  line.split(",")
       dataList = list(map(lambda v:v.replace('"',""),dataList))
       line = file.readline()      
       for v in dataList:
           print(v,end = " ")
except Exception as ex:
    print(ex)
    
