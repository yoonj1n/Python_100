a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
k = a if (a<=b) else b
print(k if k<=c else c )