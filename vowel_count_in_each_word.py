n=input().lower()
n=list(n)
c=0
l=[]
for i in range(len(n)):
    if n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u':
        c+=1

    if n[i]==' ':
        l.append(c)
        c=0
        continue
l.append(c)
print(*l)