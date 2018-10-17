a=int(input())
for _ in range(a):
    anum=map(int,input().split())

b=int(input())
for _ in range(b):
    bnum=map(int,input().split())

aSet=set(anum)
bSet=set(bnum)
print(aSet.difference(bSet),sep="\n")
print(bSet.difference(aSet),sep="\n")
