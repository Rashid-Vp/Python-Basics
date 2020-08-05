
def getArray(n,arr):
    for i in range(0,n):
        col=[]
        for i in range(0,n):
            val=int(input())
            col.append(val)
        arr.append(col)
    return arr

def displayArray(arr):
    for i in arr:
        print (i)

def main():
    arr=[]
    n=int(input("Enter the size of array: "))
    print("Enter the array values: ")
    arr=getArray(n,arr)
    print("Array elements are: ")
    displayArray(arr)

main()
