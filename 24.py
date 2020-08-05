class Area:
    def circle(self,r):
        a=3.14*r*r
        return a
        print("Circle")
    def square(self,l):
        a=l*l
        return a
        print("Square")
    def rectangle(self,l,b):
        a=l*b
        return a
        print("Rectangle")
    def triangle(self,b,h):
        a=0.5*b*h
        return a
        print("Triangle")

class MyClass(Area):
    def invalid(self):
        print("Invalid Choice!")
b=MyClass()

while True:
    print("1.Circle\n2.Square\n3.Rectangle\n4.Triangle\n5.Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        r=float(input("Enter the radius: "))
        ans=b.circle(r)
        print("Area= ",ans)
    elif n==2:
        l=float(input("Enter the length: "))
        ans=b.square(l)
        print("Area= ",ans)
    elif n==3:
        l=float(input("Enter the length: "))
        b=float(input("Enter the bridth: "))
        ans=b.rectangle(l,b)
        print("Area= ",ans)
    elif n==4:
        b=float(input("Enter the base: "))
        h=float(input("Enter the hypotenuse: "))
        ans=b.triangle(b,h)
        print("Area= ",ans)
    elif n==5:
        break
    else:
        b.invalid()