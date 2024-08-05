def c2f(c):
    f = 9 / 5 * c + 32
    return f

while True:
    inStr = input("攝氏溫度(q離開)")
    if inStr == "q":
        print("結束")
        break

    tc = float(inStr)
    print(f"華氏溫度:{c2f(tc):.2f}")
