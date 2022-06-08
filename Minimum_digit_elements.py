n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    a[i]=str(a[i])
    l.append(len(a[i]))
print(l.count(min(l)))
