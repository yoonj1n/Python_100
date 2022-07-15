a,b,c,d = input().split()
ans = int(a)
for i in range(int(d)-1):
    ans= ans*int(b)+int(c)

print(ans)