n=int(input())
l=[]
while n:
    d=n%10
    l.append(d)
    n=n//10
print(max(l))