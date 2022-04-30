t=int(input())
for i in range(t):
    n=int(input())
    s=0
    k=n
    while n:
        d=n%10
        s=(s*10)+d
        n=n//10
    if k==s:
        print("True")
    else:
        print("False")