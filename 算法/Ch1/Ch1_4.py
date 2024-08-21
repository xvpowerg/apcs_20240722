def gcd2(m,n):
    if n == 0:
        return m
    else:
        return gcd2(n,m%n)
        
print(gcd2(20,14))
