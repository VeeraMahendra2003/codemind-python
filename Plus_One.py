def plusOne(a):
    n = len(a) - 1
    while a[n] == 9:
        a[n] = 0
        n = n - 1
    if n < 0:
        a = [1] + a
    else:
        a[n] = a[n] + 1
    return a

t=int(input())
a=list(map(int,input().split()))
print(*plusOne(a))