n=input()
c=n.split()
l=[]
for i in range(len(c)):
    l.append(min(c[i]))
    l.append(max(c[i]))
print(*l)