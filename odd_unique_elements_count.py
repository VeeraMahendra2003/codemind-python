n=int(input())
a=list(map(int,input().split()))
l=[]
s=0
for i in a:
    if i not in l and i%2!=0:
        s+=1
        l.append(i)
print(s)

         