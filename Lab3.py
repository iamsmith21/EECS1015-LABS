#########
# EECS1015 Fall 2022
# Lab 3

# Task 1
print("\n---- Task 1: Simple order ----")

print("***Select munu item***")
print("(1) Coke [$1.00]")
print("(2) Dosa [$2.50]")
print("(3) Pizza [$2.25]")
print("(4) Taco [$1.50]")
print("(5) Tea [$1.00]")
usr_Inp = int(input("Selection:"))

if usr_Inp == 1:
    usr_inp = 1.00
elif usr_Inp == 2:
    usr_Inp = 2.50
elif usr_Inp == 3:
    usr_Inp = 2.25
elif usr_Inp == 4:
    usr_Inp = 1.50
elif usr_Inp == 5:
    usr_Inp = 1.00
else:
    print("Invalid Selection - setting amount to $0")
    usr_Inp = 0.00
    

print("**Discount**")
Child = "(C) Child  [under 18] (50% discount)"
Adult = "(A) Adult  [18-64]"
Senior = "(S) Senior [65+] (25% discount)"
print(Child)
print(Adult)
print(Senior)

usr_Age = input("selection age:")

if (usr_Age == "c" or usr_Age == "C"):
    discount = usr_Inp*.5
elif (usr_Age == "a" or usr_Age == "A"):
    discount = usr_Inp*0
elif (usr_Age == "s" or usr_Age == "S"):
    discount = usr_Inp*0.25
else:
    discount = usr_Inp*-.25

    

print(f"Amount $ {usr_Inp}")
print(f"Discount $ {discount:.2f}")
print("--------------------")
print(f"Total $ {usr_Inp - discount:.2f}")


# Task 2
print("\n---- Task 2: Draw circle ----")

# x2 + y2 <= r2
temp = 1

while(temp):
    userInput=int(input("Input size between 1-10: "))
    if(userInput > 0 and userInput < 11):
        temp=0

for j in range(-10,11):
    for i in range(-10,11):
        if i**2 + j**2 <= userInput**2:
            print("*", end="")
        else:
            print(".", end="")
    print()


# Task 3
print("\n---- Task 3: Dice pair expected value ----")
import random


y = 1
while True:
    num_Roll = int(input("Roll dice how many times? "))
    sumtotal = 0
    for i in range(1,num_Roll+1):
        die1 = random.randint(0,6)
        die2 = random.randint(0,6)
    
        print(f"[{die1}]    [{die2}] -- {die1+die2:2}     Roll {i}")
        i = i + 1
        sum_die = die1 + die2
        sumtotal = sumtotal + sum_die
        avg = sumtotal/num_Roll 
    print(f"Average dice pair value: {avg}")
    Rerun = input("Try Again[Y/N]")
    if Rerun == "Y" or Rerun == "y":
        y =1
    else:
        break
        
# Task 4
print("\n---- Task 4: Compute PI ----")
# task4

M = int(input("Input number of terms, M: "))



sum = 0
for n in range(0,M+1):
    Numerator = ((-1)**n)
    Denominator = (2*n + 1)
    print(f"n = {n} . . . adding fraction : {Numerator}/{Denominator}")
    
    sum +=  4*(Numerator/Denominator)
    
    print(" our  pi = %.12f"%(sum))
    print(" real pi = 3.14159265359")



# Modified 
real_Pi = 3.14159265359
uncertainty = float(input("Enter uncertainty: "))
sum = 0
n = 0
while not(abs(sum - real_Pi) <= uncertainty):
    Numerator = ((-1)**n)
    Denominator = (2*n + 1)
    term = Numerator/Denominator
    print(f"n = {n} . . . adding fraction : {Numerator}/{Denominator}")
    
    print(" our  pi = %.12f"%(4*term+sum))
    print(" real pi = 3.14159265359")

    sum = 4*term+sum
    n=n+1




# pause program until enter is pressed
print("\n---- Lab 3 Done ----")
input("Press enter to exit.")
