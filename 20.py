count=0
n=int(input("Enter the number of lines: "))
for i in range(0,n+1):
    for i in range(0,i):
        count=count+1
        print(count, end=" ")
    print("\n")