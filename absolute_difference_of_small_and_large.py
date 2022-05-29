n=input()
c=n.split()
l=[]
k=[]
r=[]
for i in range(len(c)):
    l.append(min(c[i]))
    k.append(max(c[i]))
    r.append(abs(ord(l[i])-ord(k[i])))
print(*r)
    
    