def prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    else:
        return True
n=int(input())
s=0
if prime(n):
    while n:
        d=n%10
        s=(s*10)+d
        n=n//10
    if prime(s):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")