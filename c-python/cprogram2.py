#program to add two numbers
a=5
b=10
print("a+b=",a+b)
#program to add,substract,multiply,divide two number taking from user 
print("enter 1st number:")
num1=int(input())
print("enter 2nd number:")
num2=int(input())
sum=num1+num2
mul=int(num1*num2)
div=int(num1//num2)
if num1>num2:
    sub=num1-num2
else:
    sub=num2-num1
print("sum=",sum)
print("multiplication=",mul)
print("division=",div)
print("substraction=",sub)