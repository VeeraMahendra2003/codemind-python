t=int(input())
for i in range(t):
    a=int(input())
    c=0
    for n in range(a,1,-1):
        for j in range(2,int(n**0.5)+1):
            if n%j==0:
                break
        else:
            z=n
            break
    b=a
    while a:
        for j in range(2,int(a**0.5)+1):
            if a%j==0:
                break
        else:
            x=a
            break
        a+=1
    if abs(b-n)>abs(a-b):
        print(x)
    else:
        print(z)
        