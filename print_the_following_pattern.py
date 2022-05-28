n=int(input())
for i in range(1,n+1):
    for j in range(n-1,i-1,-1):
        print(' ',end='')
    for j in range(1,i+1):
        print(i,end='')
    for j in range(1,i):
        print(i,end='')
    print()
