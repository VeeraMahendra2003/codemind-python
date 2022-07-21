def octal(x):
    s=''
    while x:
        d=x%8
        x=x//8
        s+=str(d)
    return s[::-1]
t=int(input())
for i in range(t):
    n=int(input())
    i=s=0
    while n:
        d=n%10
        s=s+((2**i)*d)
        n=n//10
        i+=1
    print(octal(s))