def prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
for x in range(1,10):
    s=n+m+x
    if prime(s):
        print(x)
        break