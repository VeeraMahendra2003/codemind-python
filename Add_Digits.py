def add(n):
    s=0
    while n:
        d=n%10
        s=s+d
        n=n//10
    return s
n=int(input())
k=add(n)
x=add(k)
y=add(x)
print(y)