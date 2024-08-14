import csv
fields = ["name","gender","score","age","ageStage","birthday"]
file = open("data2.csv","r")
csvCursor =  csv.DictReader(file,fields)
for row in csvCursor:
    print(row["gender"],row["score"])
