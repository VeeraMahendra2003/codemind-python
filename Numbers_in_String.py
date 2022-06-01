n=input()
s=0
for i in n:
    if i in '0123456789':
        s=s+int(i)
print(s)