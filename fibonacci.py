def fibo(n):
    a=0;b=1
    print(a,end=' ')
    print(b,end=' ')
    c=a+b
    for i in range(2,n):
        print(c,end=' ')
        a=b
        b=c
        c=a+b
n=int(input())
fibo(n)