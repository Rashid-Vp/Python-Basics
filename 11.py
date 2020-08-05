a=[]
flag=0
n=int(input("Enter the size of array:"))
print("Enter the values of array:")
for i in range(0,n):
    val=int(input())
    a.append(val)
for i in range(0,n):
    if a[i]%2==0:
        flag=flag+1
print("Number of even numbers in the given array is",flag)