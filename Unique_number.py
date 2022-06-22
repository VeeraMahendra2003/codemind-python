n=int(input())
s=str(n)
l=list(s)
b=set(l)
m=list(b)
x=sorted(l)
y=sorted(m)
if x==y:
    print("Unique Number")
else:
    print("Not Unique Number")
    
    