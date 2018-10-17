s=input()
i,c=input().split()
i=int(i)

l=list(s)
l[i]=c
s=''.join(l)
print(s)
