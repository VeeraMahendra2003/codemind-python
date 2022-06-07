n=input()
c=list(n)
l=[]
s=''
for i in range(len(c)):
    d=c[i]
    if int(d)%2!=0:
        t=int(d)*int(d)
        s+=str(t)
    else:
        continue
print(s)
    