h,w = input().split()
d = [[0 for i in range(int(w))] for j in range(int(h))]
n = int(input())
for i in range(n):
    l, di, x, y = input().split()
    if int(di) ==0:
        for k in range(int(l)):
            d[int(x)-1][int(y)-1+k] = 1
        
    else:
        for k in range(int(l)):
            d[int(x)-1+k][int(y)-1] = 1
            

for i in range(int(h)):
    for k in range(int(w)):
        print(d[i][k],end= ' ')
    print()