def ad(a):
    if a%2 ==0:
        print("even")
    else:
        print("odd")

a,b,c = input().split()
ad(int(a))
ad(int(b))
ad(int(c))