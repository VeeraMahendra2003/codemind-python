n=input()
c=n.split()
l=[]
k=[]
s=0
t=0
for i in range(len(c)):
    l.append(min(c[i]))
    k.append(max(c[i]))
for j in range(len(l)):
    s=s+int(ord(l[j]))
for j in range(len(k)):
    t=t+int(ord(k[j]))
print(t-s)

    
    
    