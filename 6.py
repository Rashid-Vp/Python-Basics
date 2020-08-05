n=int(input("Enter the choice: "))
switcher={
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday",
    7:"Saturday"
    }
x=switcher.get(n)
if x==None:
    print("Invalid Input")
else:
    print(x)
