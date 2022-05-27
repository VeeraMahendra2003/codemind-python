n=input()
v=d=s=c=0
for i in range(len(n)):
    if n[i] in 'aeiouAEIOU':
        v+=1
    elif n[i] in '0123456789':
        d+=1
    elif n[i] in ' ':
        s+=1
    else:
        c+=1
print("Vowels: %d"%v)
print("Consonants: %d"%c)
print("Digits: %d"%d)
print("White spaces: %d"%s)
