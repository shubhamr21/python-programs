l = [1,1,3,4,6,8,1,3,4,2,6,2,4]
a = []

for i in range(len(l)):
    if i==0:
        a.append(l[i])
    else:
        c = 0
        d = l[i]
        for j in range(len(a)):
            if(d==a[j]):
                c=1
        if(c==0):
            a.append(l[i])
print(a) 