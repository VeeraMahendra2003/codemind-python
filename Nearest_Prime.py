t=int(input())
for j in range(1,t+1):
    a=int(input())
    for n in range(a,1,-1):
        for i in range(2,int(a**0.5)+1):
            if n%i==0:
                break
        else:
            break
    b=a
    while a:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                break
        
        else:
            break
        a+=1
    if abs(b-n)>abs(a-b):
        print(a)
    else:
        print(n)