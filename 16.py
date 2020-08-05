flag=0
n=int(input("Enter a number: "))
for i in range(2,n):
    if n%i==0:
        flag=1
if flag==0:
    print("Entered number is a Prime number")
else:
    print("Entered number is Not Prime number")