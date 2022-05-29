n=input()
c=n.split()
l=[]
m=c[::-1]
d=''.join(m)
for i in range(len(d)):
    l.append(d[i])
print(*l[0])
