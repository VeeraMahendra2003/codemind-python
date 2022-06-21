n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.split()
m=m.split()
c=[]
for i in n:
    if i in m:
        c.append(i)
for i in m:
    if i in n and i not in c:
        c.append(i)
print(len(c))