a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
s = 0
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i,j,k)
            s+=1
print(s)