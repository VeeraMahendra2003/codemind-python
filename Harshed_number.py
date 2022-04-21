n=int(input())
t=n
s=0
while n:
    d=n%10
    s=s+d
    n=n//10
n=t
if n%s==0:
    print("True")
else:
    print("False")