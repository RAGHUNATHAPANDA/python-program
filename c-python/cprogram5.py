#wap to check palindrome
print("enter yor number")
a=int(input())
rev=0
p=a
while a!=0:
    digit=a%10
    a=a//10
    rev=rev*10+digit
if(p==rev):
    print("paindrom")
else:
    print("not a palindrom")
#wap to print fibonaci series
num=int(input("enetr any number:"))
n1,n2=0,1
sum=0
if num<=0:
    print("please enter number greter then 0")
else:
    for i in range(0,num):
        print(sum,end=" ")
        n1=n2
        #print("n1=",n1)
        n2=sum
        #print("n2=",n2)
        sum=n1+n2
#wap to find factorial of a number
num=int(input("enter a number:"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
print("factorial of",num,"=",factorial)
#wap to print multiplication table
num1=int(input("enter the table number:"))
b=1
while b<=10:
    c=num1*b
    print(num1,"*",b,"=",c)
    b+=1
#wap to check armstrong number
num=int(input("enter a number:")) #153
s=num
sum=0
while num!=0:
    digit=int(num%10)                 #3  5  1
    num=int(num/10)                   #35 3  0
    sum=int(sum+digit**3) 
    #print(sum)                        # 0+3**3  27+5**3  152+1**3
if sum==s:                          #153
    print("armstrong number")
else:
     print("not armstrong number")
#wap to find HCF
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
while num1%num2!=0:
    rem=num1%num2
    num1=num2
    num2=rem
print("hcf=",num2)

