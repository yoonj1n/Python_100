d = [[] for i in range(19)]
for i in range(19):
    a = input().split()
    for k in range(19):
        d[i].append(int(a[k]))

n = int(input())
for i in range(n):
    x,y = input().split()
    for k in range(19):
        if d[int(x)-1][k] ==0:
            d[int(x)-1][k] = 1
        else:
            d[int(x)-1][k] = 0
    
    for k in range(19):
        if d[k][int(y)-1] ==0:
            d[k][int(y)-1] =1
        else:
            d[k][int(y)-1] = 0


for i in range(19):
    for k in range(19):
        print(d[i][k], end =' ')
    print()