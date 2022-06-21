n=input().split(" ")
k=[]
x=n[0]
k.append(min(x))
y=n[-1]
k.append(max(y))
print(*k)