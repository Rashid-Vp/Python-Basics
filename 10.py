a=[]
b=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements of first array: ")
for i in range(0,n):
    v=input()
    a.append(v)
print("Enter the elements of second array: ")
for j in range(0,n):
    v=input()
    b.append(v)
print("Before swapping")
print("A=",a)
print("B=",b)
for i in range(0,n):
    temp=a[i]
    a[i]=b[i]
    b[i]=temp
print("After swapping")
print("A=",a)
print("B=",b)