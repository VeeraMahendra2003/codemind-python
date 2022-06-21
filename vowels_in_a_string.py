n=input()
l=list(n)
m=input()
c=0
for i in range(len(l)):
    if l[i]==m:
        m=i
        c+=1
        
if c==0:
    print(False)
else:
    print(True)
    print(m)