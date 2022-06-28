n=int(input())
a=list(map(int,input().split()))
s=0
b=[]
for i in a:
    if i not in b:
        s+=i
        b.append(i)
        
print(s)