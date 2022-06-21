n=int(input())
a=list(map(int,input().split()))
l=[]
k=[]
for i in range(len(a)):
    if a[i]%2!=0:
        l.append(a[i])
    elif a[i]%2==0:
        k.append(a[i])
print(*l,end=' ')
print(*k,end='')
