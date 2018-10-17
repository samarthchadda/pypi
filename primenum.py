num=int(input("Enter the number:"))
c=0
for i in range(1,num+1):
    if(num%i)==0:
        c=c+1

if(c==2):
    print(num," is prime number")
else:
    print(num," is not prime number")
    
