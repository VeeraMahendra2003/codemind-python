n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(len(a)):
    s=s+a[i]
avg=s//n
c=0
for i in range(len(a)):
    if a[i]==avg:
        c+=1
if c==0:
    print(False)
else:
    print(True)