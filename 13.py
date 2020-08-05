flag=0
b=[]
ch=input("Enter the string:")
l=len(ch)
for i in range(0,l):
    b.append(ch[l-(i+1)])
for i in range(0,l):
    if ch[i]!=b[i]:
        flag=1
if flag==0:
    print("Entered string is a palindrome")
else:
    print("Entered string is not a palindrome")