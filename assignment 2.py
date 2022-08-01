
#Question 1 -  WAP to accept a signed integer and display both its sign and value

num=int(input("Enter a signed number="))
a=-(num)
if num<0:
    print("value=",a,"and sign= -")
else:
    print("value=",num,"and sign= +")

#Question 2 - Check whether a year is a leap year or not

num=int(input("Enter a year="))
if (num % 400==0) or (num % 100!=0 and num % 4==0):
    print("It is a Leap Year")
else:
    print("It is not a Leap year")

#Question 3 - WAP to find the smallest number among 3 numbers

num_1=int(input("Enter the first number="))
num_2=int(input("Enter the second number="))
num_3=int(input("Enter the third number="))
if num_1<num_2 and num_1<num_3:
    print(" ",num_1,"is the smallest number")
if num_2<num_1 and num_2<num_3:
    print(" ",num_2,"is the smallest number")
if num_3<num_1 and num_3<num_2:
    print(" ",num_3,"is the smallest number")

#Question 4 - Check number is even or odd

num=int(input("Enter a number="))
if num>=0 and num%2==0:
    print("",num,"is even number")
if num>=1 and num%2!=0:
    print("",num,"is odd number")

#Question 5 - WAP to find the the real roots
 
import math
a=float(input("Enter the first coefficient ="))
b=float(input("Enter the second coefficient ="))
c=float(input("Enter the third coefficient ="))
d=(b*b)-(4*a*c)
if d>0 or d==0:
    print("The roots are real")
    x_1=(-b+math.sqrt(d))/2*a
    x_2=(-b-math.sqrt(d))/2*a
    print("The roots are ",x_1,"and ",x_2)
else:
    print("The roots are imaginary")

#Question 6 - ATM money withdraw problem

amt=int(input("Enter the amount = "))
va_1=int(amt / 100)
va_5=int(amt / 500)
if amt%100==0 or amt%500==0:
    print("if withdraw amount request is: ",amt)
    print("100's currency = ",va_1)
    print("500's currency = ",va_5)
else:
    print("if withdraw amount request is: ",amt)
    print("Invalid amount. Not multiple of 100")

#Question 7 - WAP to check Armstrong number

num=int(input("Enter the number = "))
temp=num
sum=0
while temp!=0:
    x=temp % 10
    sum=sum+(x**3)
    temp=temp//10
if sum==num:
    print("",num,"is an armstrong number")
else:
    print("",num,"is not an armstrong number")

#Question 8 - WAP to convert lower case character to uppercase character

a=input("Enter a character = ")
print("Input = ",a)
if(a==a.lower()):
    print("Output = ",a.upper())
if(a==a.upper()):
    print("Output = ",a.lower())
if(a!=a.lower() and a!=a.upper()):
    print("Output = ",a)

#Question 9 - WAP that will accept basic payof an employee then calculate the gross pay and net pay

def func(x,t):
    np=x-t
    print("Net Pay = ",np)

bp=float(input("Enter the basic pay of an employee = Rs"))
if bp<12000:
    hra=(10/100)*bp
    da=(50/100)*bp
    gp=bp+hra+da
    tax=0
    print("Basic Pay = ",bp)
    print("Gross Pay = ",gp)
    func(gp,tax)
if 12000<=bp<30000:
    hra=(15/100)*bp
    da=(55/100)*bp
    gp=bp+hra+da
    tax=(12/100)*gp
    print("Basic Pay = ",bp)
    print("Gross Pay = ",gp)
    func(gp,tax)
if bp>=30000:
    hra=(20/100)*bp
    da=(60/100)*bp
    gp=bp+hra+da
    tax=(15/100)*gp
    print("Basic Pay = ",bp)
    print("Gross Pay = ",gp)
    func(gp,tax)

#Question 10 - Calculate and display percentage and grade of a student

def func(ag,tot):
    perc=int((ag/tot)*100)
    if 90<=perc<=100:
        print("",perc,("% of Marks is Grade A+"))
    if 80<=perc<90:
        print("",perc,("% of Marks is Grade A"))
    if 70<=perc<80:
        print("",perc,("% of Marks is Grade B+"))
    if 60<=perc<70:
        print("",perc,("% of Marks is Grade B"))
    if 50<=perc<60:
        print("",perc,("% of Marks is Grade C"))
    if perc<50:
        print("",perc,("% of Marks is Grade F"))

am=int(input("Enter the aggregate marks = "))
tm=int(input("Enter the total marks = "))
func(am,tm)    

#Question 11 - Menu based program

print("Menu")
print("1. Monday")
print("2. Tuesday")
print("3. Wednesday")
print("4. Thursday")
print("5. Friday")
print("6. Saturday")
print("7. Sunday")
choice=int(input("Enter any number between 1 to 7 :"))

if choice==1:
    print("Monday")
elif choice==2:
    print("Tuesday")
elif choice==3:
    print("Wednesday")
elif choice==4:
    print("Thursday")
elif choice==5:
    print("Friday")
elif choice==6:
    print("Saturday")
elif choice==7:
    print("Sunday")
else:
    print("Enter Valid Input")

#Question 12 - WAP for a menu based calculator

def add(a,b):
    r=a+b
    print("Addition of ",a,"and ",b,"is =",r)

def sub(a,b):
    r=a-b
    print("Subtraction of ",a,"and ",b,"is =",r)

def mul(a,b):
    r=a*b
    print("Multiplication of ",a,"and ",b,"is =",r)

def div(a,b):
    r=a/b
    print("Division of ",a,"and ",b,"is =",r)

print("Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=int(input("Enter any option :"))

if choice==1:
    print("Addition")
    a=float(input("Enter first number = "))
    b=float(input("Enter second number = "))
    add(a,b)
elif choice==2:
    print("Subtraction")
    a=float(input("Enter first number = "))
    b=float(input("Enter second number = "))
    sub(a,b)
elif choice==3:
    print("Multiplication")
    a=float(input("Enter first number = "))
    b=float(input("Enter second number = "))
    mul(a,b)
elif choice==4:
    print("Division")
    a=float(input("Enter first number = "))
    b=float(input("Enter second number = "))
    div(a,b)
else:
    print("Enter valid option")


