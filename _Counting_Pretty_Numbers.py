def pretty(x):
    l=[]
    while x:
        d=x%10
        if d==2 or d==3 or d==9:
            l.append(d)
        break
        x=x//10
    return l
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    c=0
    for i in range(n,m+1):
        if pretty(i):
            c+=1
    print(c)