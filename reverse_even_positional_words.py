n=input()
c=n.split()
l=[]
for i in range(len(c)):
    if i%2==0:
        l.append(c[i][::-1])
    else:
        l.append(c[i])
print(*l)
        
        