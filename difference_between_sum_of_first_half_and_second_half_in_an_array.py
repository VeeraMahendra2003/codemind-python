n=int(input())
a=list(map(int,input().split()))
s=0
k=0
for i in range(len(a)//2):
    s=s+a[i]
for i in range(len(a)//2,len(a)):
    k=k+a[i]
print(k-s)
    