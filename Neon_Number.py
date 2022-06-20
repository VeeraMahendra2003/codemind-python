n=int(input())
t=n
x=n**2
s=0
while x:
    d=x%10
    s=s+d
    x=x//10
if s==t:
    print('Neon Number')
else:
    print('Not Neon Number')