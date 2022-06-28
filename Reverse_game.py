n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,len(a)):
    t=a[i]
    s=0
    while t:
        d=t%10
        s=(s*10)+d
        t=t//10
    l.append(s)
print(*l)