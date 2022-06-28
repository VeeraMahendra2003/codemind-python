n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in range(len(a)):
    if a[i]<=k:
        s=s+a[i]
print(s)