#wap to find HCF
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
while num1%num2!=0:
    rem=num1%num2
    num1=num2
    num2=rem
print("hcf=",num2)

