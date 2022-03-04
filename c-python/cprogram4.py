# wap to find greast among three numbers
print("enter your 1st number")
num1=int(input())
print("enter your 2nd number")
num2=int(input())
print("enter your 3rd number")
num3=int(input())
if num1>num2 and num2>num3:
    print("num1 is greter than nu2 and num3")
elif num2>num1 and num1>num3:
    print("num2 greater than num1 and num3")
else:
    print("num3 is greater then num1 and num2")

#display the dayb according to the number
from ast import Pass
print("choice a number among 1 to 7")
num4=int(input())
if num4==1:
    print("monday")
elif num4==2:
    print("tuesday")
elif num4==3:
    print("wednesday")
elif num4==4:
    print("thursday")
elif num4==5:
    print("friday")
elif num4==6:
    print("saturday")
elif num4==7:
    print("sunday")
else:
    Pass
#write a program to print 1 to 10 using while loop-
i=1
while i<=10:
    print(i)
    i+=1
#wap a program to check prime number
print("enter ba number")
number=int(input())
if number > 1:
    for i in range(2, number):
        print("i=",i)
        if (number % i) == 0:
            print("num%i=",number%i)
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")
#wap to print all the even numbers between 1 to 100 in while loop
i=0
while i<=100:
    if i%2==0:
        print(i,end=" ")
    else:
        print(end="")
    i+=1
#wrp to find sum of digit of a number
print("enter a number")
num5=int(input())
sum=0
while (num5!=0):
    digit=int(num5%10)
    print ("digit=",digit)
    num5=int(num5/10)
    print("num5",num5)
    sum+=digit
    print("sum",sum)
print("sum of digit=",int(sum))
#wap to revers a number
print("enter your 1st number")
num6=int(input())
while(num6!=0):
    digit=int(num6%10)
    num6=int(num6/10)
    print(digit,end=" ")
