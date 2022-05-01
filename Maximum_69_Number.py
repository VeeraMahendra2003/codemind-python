num=input()
num=list(num)
for i in range(0,len(num)):
    if num[i]=='6':
        num[i]='9'
        break;
num="".join(num)
print(num)
    