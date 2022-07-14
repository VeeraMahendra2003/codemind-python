n,m=map(int,input().split())
l=[]
k=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
for i in range(n):
    s=0
    for j in range(m):
        if i%2==0 or i%2!=0:
            s=s+l[i][j]
    k.append(s)
print(max(k))
        