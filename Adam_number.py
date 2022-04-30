def rev(n):
    s=0
    while(n):
        d=n%10
        s=(s*10)+d
        n=n//10
    return s
n=int(input())
t=n*n
k=rev(n)
z=k*k
x=rev(z)
if t==x:
    print("True")
else:
    print("False")