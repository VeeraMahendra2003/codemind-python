t=int(input())
a=list(map(int,input().split()))
n,m=map(int,input().split())
l=[]
for i in range(len(a)):
    if a[i]>=n and a[i]<=m:
        continue
    else:
        l.append(a[i])
if len(l)==0:
    print("-1")
else:
    print(min(l))

         