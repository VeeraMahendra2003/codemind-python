def rev(n):
    s=0
    while n:
        d=n%10
        s=(s*10)+d
        n=n//10
    return s
n=int(input())
a=rev(n)
print(a)