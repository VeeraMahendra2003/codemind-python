n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(len(a)):
    m=a[i]*a[i];
    l.append(m)
print(*sorted(l))