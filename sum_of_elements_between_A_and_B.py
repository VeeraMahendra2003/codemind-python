n=int(input())
a=list(map(int,input().split()))
g,h=map(int,input().split())
s=0
for i in range(len(a)):
    if a[i]>=g and a[i]<=h:
        s=s+a[i]
print(s)