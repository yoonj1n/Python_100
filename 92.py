n = int(input())
a = input().split()
d = [0 for i in range(23)]
for i in range(n):
    a[i] = int(a[i])
    d[a[i]-1]+=1

for i in d:
    print(i,end=' ')

