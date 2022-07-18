n = int(input())
a = input().split()
min = int(a[0])
for i in range(n):
    a[i] = int(a[i])
    if min>=a[i]:
        min = a[i]
print(min)