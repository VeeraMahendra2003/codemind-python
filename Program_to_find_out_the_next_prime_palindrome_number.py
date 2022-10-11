def prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def palin(y):
    a=y
    s=0
    while a:
        d=a%10
        s=(s*10)+d
        a=a//10
    if s==y:
        return True
    else:
        return False
n=int(input())
for i in range(n+1,n*n,+1):
    if prime(i) and palin(i):
        print(i)
        break