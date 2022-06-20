n=input()
s=n.split()
l=list(s)
k=[]
for i in range(len(l)):
    if i%2==0:
        m=l[i][::-1]
        k.append(m)
    else:
        k.append(l[i])
print(*k)