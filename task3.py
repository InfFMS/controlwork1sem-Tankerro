def F(n):
    if n > 1:
        Ans = F(n-1)+2**(n-1)
    else:
        return 1
    return Ans
print(F(12))