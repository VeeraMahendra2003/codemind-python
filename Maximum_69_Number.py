n=input()
l=list(n)
for i in range(0,len(l)):
    if l[i]=='6':
       l[i]='9'
       break
d=''.join(l)
print(d)