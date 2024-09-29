#Basic Calculator Program by using Functions and "if else"--------->
def Addition(a, b):
    Sum = a+b
    print(Sum)
def Subtraction(a, b):
    Sub=a-b
    print(Sub)
def Multiplication(a, b):
    Mul=a*b
    print(Mul)
def Division(a, b):
    Div=a/b
    print(Div)
a=int(input("Enter 1st Number: "))
b=int(input("Enter 2st Number: "))
print("Choose operation do you want to perform :")
print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")
con = int(input("---->"))
if con == 1:
    Addition(a,b)
elif con == 2:
    Subtraction(a,b)
elif con == 3:
    Multiplication(a,b)
elif con == 4:
    Division(a,b)
else:
    print("This Operation is not yet available")