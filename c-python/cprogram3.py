# program to check even or odd
print("enter number:")
a=int(input())  
#print(type(a))
c=a%2
if c!=0:
    print("odd")
else:
    print("even")

# wap to check the +ve and -ve numbers
print("enter number:")
num=int(input())
if (num>0):
    print("+ve number")
else:
    print("-ve number")
#wap to find greater among two number
print("enter 1st number:")
num1=input()
print("enter 2nd number:")
num2=input()
if num1>num2:
    print("num1 is greater then num2")
else:
    print("num2 greater than num1")
#wap to decide the grade according to mark
print("enter your mark")
mark=int(input())
if mark>90 and mark<100:
    print("O grade")
elif mark>80 and mark<90:
    print("E grade")
elif mark>=70 and mark<80:
    print("A grade")
elif mark>60 and mark<70:
    print("B grade")
elif mark>50 and mark<60:
    print("C grade")
elif mark>40 and mark<50:
    print("D grade")
else:
    print("F grade")