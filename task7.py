for i in range(1000, 10000):
    N = 0
    s12 = int(str(i)[0]) + int(str(i)[1])
    s23 = int(str(i)[1]) + int(str(i)[2])
    s34 = int(str(i)[2]) + int(str(i)[3])
    s1 = max(s12, s23, s34)
    if s1 == s12:
        s2 = max(s23, s34)
    elif s1 == s23:
        s2 = max(s12, s34)
    elif s1 == s34:
        s2 = max(s12, s23)
    N = int(str(s1) + str(s2))
    if N == 1214:
        print(N)
        break
