n=input()
m=input()
c=0
for i in range(len(n)):
    if n[i] in m:
        c+=1
    
if c==0:
    print("-1")
else:
    print(c)