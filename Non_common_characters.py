n=input().lower()
m=input().lower()
n=set(n)
m=set(m)
c=k=0
for i in n:
    if i not in m and i!=' ':
        c+=1
for i in m:
    if i not in n and i!=' ':
        k+=1
print(c+k)