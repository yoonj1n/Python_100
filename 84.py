a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
ans = a*b*c*d/8/1024/1024
print(format(ans,".1f"), "MB")