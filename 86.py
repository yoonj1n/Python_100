i = int(input())
sum = 0
for k in range(i+1):
    if sum < i:
        sum+=k
    else:
        break
print(sum)