a=[]
b=[]
big=0
n=int(input("Enter the size of an array:"))
print("Enter the values of array")
for i in range(0,n):
    val=int(input())
    a.append(val)
for i in range(0,n):
    for j in range(i,n):
        if a[i]<a[j]:
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
print(a)