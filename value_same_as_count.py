n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in range(len(a)):
    if a.count(a[i])==a[i]:
         l.append(a[i])
l=set(l)
print(len(l))
        
    