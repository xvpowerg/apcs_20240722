import csv

file = open("data2.csv","r")
csvCursor = csv.reader(file)
sum1 = 0.0
sum2 = 0
for row in csvCursor:
 
    try:
        sum1 += float(row[2])
        sum2 += int(row[3])
    except Exception as ex:
        print(ex,float(row[2]),int(row[3]))                
file.close()
print(f"sum1:{sum1:.2f}","sum2:",sum2)
