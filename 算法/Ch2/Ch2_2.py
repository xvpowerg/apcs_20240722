def dec_to_bin(num):
    result = []
    while True:
        num,reminder = divmod(num,2)
        result.append(str(reminder))
        if num == 0:
            return "".join(result[::-1])        
def dec_to_oct(num):
    result = []
    while True:
        num,reminder = divmod(num,8)
        result.append(str(reminder))
        if num == 0:
            return "".join(result[::-1])

def dec_to_hex(num):
    base = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    result = []
    while True:
        num,reminder = divmod(num,16)
        result.append(base[reminder])
        if  num == 0:
            return "".join(result[::-1])
        
v1 = dec_to_bin(18)
print(v1)
v2 = dec_to_oct(12)
print(v2)
v3 = dec_to_hex(30)
print(v3)
