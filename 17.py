def addition(a,b):
    c=a+b
    return c
def subtraction(a,b):
    c=a-b
    return c
def multiplication(a,b):
    c=a*b
    return c
def division(a,b):
    c=a/b
    return c
a=float(input("Enter the First number"))
b=float(input("Enter the Second number"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
n=int(input("Enter the option:"))
if n==1:
    c=addition(a,b)
    print("Ans: ",c)
elif n==2:
    c=subtraction(a,b)
    print("Ans: ",c)
elif n==3:
    c=multiplication(a,b)
    print("Ans: ",c)
elif n==4:
    c=division(a,b)
    print("Ans: ",c)
else:
    print("Invalid Option")