n=input()
s=n.split()
l=list(s)
k=[]
for i in range(len(l)):
    m=l[i][::-1]
    k.append(m)
print(*k)