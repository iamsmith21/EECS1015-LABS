########################################
# EECS1015- Fall 2022
# Lab 1
#######################################

# Please fill out your info for each lab 
# Task 1
print('\n---- Task 1: Currency converter ----')
a = float(input("Amount in Canadian Dollars:"))

USD = a*0.76
EUR = a*0.75
NGN = a*322.24
CNY = a*5.25
INR = a*97.14

print("Amount in other currencies:")
print("USD", USD)
print("EUR", EUR)
print("NGN", NGN)
print("CNY", CNY)
print("INR", INR)

# Task 2
print('\n---- Task 2: String math ----')
a = input("str1:")
b = input("str2:")
c = input("str3:")

print("String Concatenation:")

print("str1+str2+str3:", a+b+c)
print("str3+str2+str1:", c+b+a)
print("str2+str1+str3:", b+a+c)

num = int(input("Input an Integer"))

print("String Multiply:")

print(num*a)
print(num*(a+b))


# Task 3
print("\n---- Task 3: Math operators ----")
print("Enter two numbers")
x = int(input("Enter integer x:"))
y = int(input("Enter integer y:"))

print("Integer Math:")

print("x/y=", x/y)
print("x//y=",x//y)
print("x%y=",x%y)
print("x**y=", x**y)

print("Enter two numbers")
x = float(input("Enter float x:"))
y = float(input("Enter float y:"))

print("Float Math:")

print("x/y=", x/y)
print("x//y=",x//y)
print("x%y=",x%y)
print("x**y=", x**y)




# Task 4
print('\n---- Task 4: Simple cylinder computation ----')
r = float(input("Enter radius of cylinder:"))
h = float(input("Enter height of cylinder:"))
pi = (355/113)
SA = 2*pi*r*h + 2*pi*r*r

Vol = pi*r*r*h

print("Cylinder Surface Area: ", SA)

print("Cylinder Volume:", Vol)



## Adding the final "input" causes python to wait on the user to press enter
## before exiting the program.
print("\n---- FINISHED ----")
input("Press enter to end.")
