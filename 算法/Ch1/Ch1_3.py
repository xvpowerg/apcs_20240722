def gcd_for(m,n):
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

print(gcd_for(20,14))
