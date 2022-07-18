d = [[0 for i in range(19)] for k in range(19)]
n = int(input())
for i in range(n):
    x,y = input().split()
    d[int(x)-1][int(y)-1] = 1

for i in range(19):
    for k in range(19):
        print(d[i][k], end =' ')
    print()

