arr1=[]
arr2=[]
sum_arr=[]
n=int(input("Enter the size of arrays:"))
print("Enter the values of matrix 1: ")
for i in range(0,n):
    col1=[]
    for j in range(0,n):
        val=int(input())
        col1.append(val)
    arr1.append(col1)

print("Enter the values of matrix 2: ")
for i in range(0,n):
    col2=[]
    for j in range(0,n):
        val=int(input())
        col2.append(val)
    arr2.append(col2)

for i in range(0,n):
    col3=[]
    for j in range(0,n):
        val=arr1[i][j]+arr2[i][j]
        col3.append(val)
    sum_arr.append(col3)

for i in sum_arr:
    print (i)