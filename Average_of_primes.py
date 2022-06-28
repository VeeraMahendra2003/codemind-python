def prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        return True
    
n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in a:
    if prime(i):
        c+=1
        s=s+i
avg=s/c
print("%.2f"%avg)