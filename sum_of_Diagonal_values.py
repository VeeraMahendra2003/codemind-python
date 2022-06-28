n,m=map(int,input().split())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
n1=n-1
s=0
for i in range(len(a)):
    for j in range(len(a)):
        if i==j or j==n1:
            s=s+l[i][j]
    n1-=1
print(s)