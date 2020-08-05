inc=float(input("Enter the annual income: "))
if inc<250000:
    print("No Tax Need to Pay")
elif inc<500000:
    x=(5*inc)/100
    print("Income tax amount: ",x)
elif inc<1000000:
    x=(5*inc)/100
    print("Income tax amount: ",x)
elif inc<5000000:
    x=(5*inc)/100
    print("Income tax amount: ",x)
else:
    print("Data not availabe")