s = int(input())
sum =0
for i in range(s+1):
    if sum+i<s:
        sum+=i
    else:
        print(i)
        break