t=int(input())
a=list(map(int,input().split()))
n,m=map(int,input().split())
l=[]
k=[]
c=0
for i in range(len(a)):
    if a[i]>=n and a[i]<=m:
        l.append(a[i])
    else:
        c+=1
        k.append(a[i])
if c>0:  
     print(*k,end=' ')
else:
    print("-1")
