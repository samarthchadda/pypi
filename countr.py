from collections import Counter
n=int(input())
lst=map(int,input().split())
listc=Counter(lst)
numcust=int(input())
count=0
for i in range(numcust):
    size,price= map(int,input().split())
    if listc[size]:
        count+=price
        listc[size]-=1
    
print(count)
        
