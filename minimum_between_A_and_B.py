n=int(input())
a=list(map(int,input().split()))
g,h=map(int,input().split())
l=[]
for i in range(len(a)):
    if a[i]>=g and a[i]<=h:
        l.append(a[i])
if len(l)==0:
    print("-1")
else:
    print(min(l))