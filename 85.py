a,b,c =input().split()
ans = int(a)*int(b)*int(c)/8/1024/1024
print(format(ans,".2f"),"MB")