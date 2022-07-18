d=[]
for i in range(10):
    tmp = map(int, input().split())
    tmp = list(tmp)
    d.append(tmp)

x=1
y=1

def move(x,y):
    d[y][x] = 9
    
    if d[y][x+1]==0:
        return move(x+1,y)
    elif d[y+1][x]==0:
        return move(x,y+1)
    elif d[y][x+1]==2:
        d[y][x+1]=9
        return x+1,y
    elif d[y+1][x]==2:
        d[y+1][x]=9
        return x,y+1
    else:
        return x,y

rex,rey = move(x,y)

for i in range(10):
    for k in range(10):
        print(d[i][k],end =' ')
    print()