n=input().lower()
m=input().lower()
l=[]
n=set(n)
m=set(m)
for i in n:
    if i not in m and i!=' ':
        l.append(i)
for i in m:
    if i not in n and i!=' ':
        l.append(i)
l=sorted(l)
d=''.join(l)
print(d)