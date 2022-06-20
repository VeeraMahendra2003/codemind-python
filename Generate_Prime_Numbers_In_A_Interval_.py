def prime(x):
    l=[]
    if x==0 or x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        l.append(x)
    return l
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if prime(i):
        print(i)