n=input()
n=n.split()
c=0
mX=0
for i in range(len(n)):
    c=0
    for j in n[i]:
        if j in 'aeiouAEIOU':
            c+=1
    if c>mX:
        mX=c        
print(mX)