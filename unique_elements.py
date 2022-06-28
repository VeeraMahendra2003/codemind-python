n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    if a[i] not in l:
        l.append(a[i])
print(*l)