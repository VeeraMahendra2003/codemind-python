def add(s):
    c=0
    while s:
        d=s%10
        c=c+d
        s=s//10
    return c
n=int(input())
s=0
while n:
    d=n%10
    s=s+d
    n=n//10
t=add(s)
z=add(t)
print(z)