n=input()
n=n.lower()
n=n.split()
l=list(n)
c=0
for i in l:
    if i[0] in 'aeiou' and i[-1] not in 'aeiou':
        c+=1
print(c)