n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(a[i]+b[i])
print(*l)