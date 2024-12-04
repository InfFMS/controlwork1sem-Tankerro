a = 174457
b = 174505
k = 0
M=[]

def Quick_sort(Mass):
    if len(Mass) <= 1:
        return Mass
    k = Mass[len(Mass)//2][0]
    More = []
    Less = []
    Equal = []
    for i in range(0, len(Mass)):
        if Mass[i][0] > k:
            More.append(Mass[i])
        elif Mass[i][0] < k:
            Less.append(Mass[i])
        else:
            Equal.append(Mass[i])

    return Quick_sort(Less) + Equal + Quick_sort(More)

for i in range(a+1,b):
    m = []
    for j in range(2,i):
        if i % j == 0:
            m.append(j)
    if len(m) == 2:
        M.append([m[0]*m[1], m])

print(Quick_sort(M))
M = Quick_sort(M)
i=0
for i in range(0, len(M)):
    print(M[i][1][0], M[i][1][1])

