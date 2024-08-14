import locale
print(locale.getpreferredencoding())
fin1 =  open("Poem.txt",encoding="cp950")
line = fin1.readline()
while line:
    print(line,end="")
    line = fin1.readline()
fin1.close()


fin2 = open("PoemUTF8.txt",encoding="utf-8")
line =  fin2.readline()
while line:
    print(line,end="")
    line =  fin2.readline()
    
