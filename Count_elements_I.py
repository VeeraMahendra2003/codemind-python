n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
c=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j] and a[i] not in l:
            c+=1
            l.append(a[i])
print(c)