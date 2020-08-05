a=[]
b=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0,n):
    val=int(input())
    a.append(val)
print("A=",a)
for i in range(0,n-1):
    b.append((a[i])*(a[i+1]))
print("B=",b)