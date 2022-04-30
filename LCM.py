def hcf(n,m):
    if m==0:
        return n
    else:
        return hcf(m,n%m)
n,m=map(int,input().split())
k=hcf(n,m)
lcm=(n*m)/k
print(int(lcm))