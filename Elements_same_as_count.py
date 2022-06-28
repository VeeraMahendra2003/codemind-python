n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,n):
    if a.count(a[i])==a[i] and a[i] not in l:
        l.append(a[i])
if len(l)>0:
    print(*l)
else:
    print('-1')