arr=[]
def getArray(n):
    print("Enter the array elements")
    for i in range(0,n):
        val=input()
        arr.append(val)
    return arr
def displayArray(arr):
    print(arr)
n=int(input("Enter the size of array:"))
arr=getArray(n)
displayArray(arr)