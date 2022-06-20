def rev(m):
    s=0
    while m:
        d=m%10
        s=(s*10)+d
        m=m//10
    return s
n=int(input())  
t=n**2          
a=rev(n)        
x=a**2          
z=rev(x)
if t==z:
     print(True)
else:
    print(False)