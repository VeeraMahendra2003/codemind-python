n=int(input())
m=int(input())
s=0
c=0
for i in range(1,n):
    if n%i==0:
        s=s+i
for j in range(1,m):
    if m%j==0:
        c=c+j
if n==c and m==s:
    print('Amicable')
else:
    print('Not Amicable')