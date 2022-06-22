import math
p,t,r=map(int,input().split())
c=math.pow(1+t/100,r)
c=c*p
print("%.2f"%c)