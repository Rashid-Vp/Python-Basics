arr1=[]
arr2=[]
sum_arr=[]
def getArray(n):
    arr=[]
    for i in range(0,n):
        col1=[]
        for j in range(0,n):
            val=int(input())
            col1.append(val)
        arr.append(col1)

    return arr

def addArray(arr1,arr2):
    for i in range(0,n):
        col2=[]
        for j in range(0,n):
            val=arr1[i][j]+arr2[i][j]
            col2.append(val)
        sum_arr.append(col2)
    return sum_arr

def displayArray(sum_arr):
    for i in sum_arr:
        print (i)

n=int(input("Enter the size of array: "))
print("Enter the first matrix: ")
arr1=getArray(n)
print("Enter the second matrix: ")
arr2=getArray(n)

sum_arr=addArray(arr1,arr2)

print("Sum of matrix1 and matrix2:")
displayArray(sum_arr)