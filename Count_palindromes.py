n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in range(0,len(a)):
    t=a[i]
    s=0
    while t:
        d=t%10
        s=(s*10)+d
        t=t//10
    if s==a[i]:
        c+=1
print(c)
    