def fact(d):
    p=1
    for i in range(1,d+1):
        p=p*i
    return p
n=int(input())
t=n
s=0
while n:
    d=n%10
    s=s+fact(d)
    n=n//10
if s==t:
    print("The number %d is a strong number"%s)
else:
    print("The number %d is not a strong number"%t)