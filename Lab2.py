#########
# EECS1015 Fall 2022
# Lab 2

# Task 1
print("\n---- Task 1: Three year investment return ----")
user_Name = input("Name: ").strip().title()

init_Amt = float(input("Initial Amount:$ "))
rate_Return = int(input("Rate of return: % "))

print(f"Client: {user_Name}, yearly rate of return multiplier: {rate_Return/100}")

new_Amt = init_Amt + init_Amt*(rate_Return/100)
Year_1 = print(f"Year 1\tStarting Amount: ${init_Amt:8.2f}\t\tEnding Amount: ${new_Amt:8.2f}")

new_Amt_2 = new_Amt + new_Amt*(rate_Return/100)
Year_2 = print(f"Year 2\tStarting Amount: ${new_Amt:8.2f}\t\tEnding Amount: ${new_Amt_2:8.2f}")

new_Amt_3 = new_Amt_2 + new_Amt_2*(rate_Return/100)
Year_3 = print(f"Year 3\tStarting Amount: ${new_Amt_2:8.2f}\t\tEnding Amount: ${new_Amt_3:8.2f}")


# Task 2
print("\n----Task 2 Leetspeak converter ----")
str1 = input("Type a long string: ")

print(str1.upper().replace("T","7").replace("A","^").replace("E","3").replace("I","!").replace("B","8").replace("O",".").replace("C","<").replace("S","$"))


# Task 3
print("\n---- Task 3: Substring highlighter ----")    
long_String = input("Type a sentence at the prompt below: ")

sub_String = input("Enter substring below to highlight: ")

print(f"Sentence has {len(long_String)} characters, substring has {len(sub_String)} characters.")

a = long_String.find(sub_String)
print("Substring highlighted: ")
print("{}{}{}".format(long_String[:a], "*" + sub_String.upper() + "*", long_String[a+len(sub_String):]))


# Task 4
print("\n---- Task 4: Exponent ----")
inp_Exp = input("Input exponent in the form of x^y: ".replace("^", " "))

a =int(inp_Exp[0])
b =int(inp_Exp[2:])
print(f"Extracted numbers {a} {b}")
print(a**b)

# pause program until enter is pressed
print("\n---- Lab 2 Done ----")
input("Press enter to exit.")
