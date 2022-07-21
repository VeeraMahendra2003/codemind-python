n=input().lower()
m=input().lower()
n=set(n)
m=set(m)
c=0
for i in n:
    if i in m and i!=' ':
        c+=1
print(c)