n=int(input("Enter the limit: "))
i=1
s=0
while i<=n:
    if i%2!=0:
        s=s+i
    i=i+1
print("Sum of odd numbers: ",s)