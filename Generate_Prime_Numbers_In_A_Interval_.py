def prime(x):
    if x==1 or x==0:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
for i in range(n,m+1):
    if prime(i):
        print(i)