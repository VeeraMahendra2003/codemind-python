n=int(input())
a=list(map(int,input().split()))
l=[]
s=0
for i in range(len(a)):
    if a[i] not in l:
        s=s+a[i]
        l.append(a[i])
print(s)

         