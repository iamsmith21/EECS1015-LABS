################################
# EECS1015 York Univresity
# Lab 4 - Starter Code
# Name: Smith Patel
# Section B
# Student id: 219347301
# Email:smith04@my.yorku.ca
################################

import random
import time
global num_of_jumps

def print_student_info():
    print("Name: Smith Patel")
    print("Section B")
    print("Student id: 219347301")
    print("Email: smith04@my.yorku.ca")

def get_int_input(prompt, min_value, max_value):
        while (True):
            x = int(input(prompt))
            if x <= max_value and x >= min_value:
                return x

def get_yes(prompt):
        while (True):
            x = input(prompt).upper()
            if x == 'N':
                return False
            elif x == 'Y':
                return True

def draw_owl(position, randomize):
        eye1 = '{o,o}'
        eye2 = '{-,o}'
        eye3 = '{o,-}'
        body = '/)_) '
        feet = ' " " '
        if randomize:
            rndint = random.randint(1, 3)
            if rndint == 1:
                print(" " * position + eye1)
            if rndint == 2:
                print(" " * position + eye2)
            if rndint == 3:
                print(" " * position + eye3)
        else:
            print(" " * position + eye1)
        print(" " * position + body)
        print(" " * position + feet)

def get_float_input(prompt, min_value, max_value):
    while (True):
        x = float(input(prompt))
        if x >= min_value and x <= max_value:
            return x

def compute_return(amount, rate, years):
    for i in range(years):
        amount = amount + amount * rate
    return amount

def task1():

    prompt = "How many times to move [2-20]?"
    inp_usr = get_int_input(prompt, 2, 20)

    prompt = "How long to delay [1-1000ms]? "
    inp_time = get_int_input(prompt, 1, 1000)

    prompt = "Randomize [Y/N]? "
    inp_rand = get_yes(prompt)

    for i in range(0, inp_usr):
        draw_owl(i, inp_rand)
        time.sleep(inp_time / 1000)


def task2():
    

    while (True):
        prompt = "Input initial investment amount [1, 10000]? "
        init_amt = get_float_input(prompt, 1, 10000)

        prompt = "Annual return rate [0-1]? "
        rate_of_return = get_float_input(prompt, 0, 1)

        prompt = "How many years [1-10]? "
        num_of_years = get_int_input(prompt, 1, 10)

        if num_of_years > 1:
            print_result = "Return in " + str(num_of_years) + " years is: $"
            new_amount = compute_return(init_amt, rate_of_return, num_of_years)
            print(print_result, f"%10.2f" % new_amount)
        elif num_of_years == 1:
            print_result = "Return in " + str(num_of_years) + " year is: $"
            new_amount = compute_return(init_amt, rate_of_return, num_of_years)
            print(print_result, f"%10.2f" % new_amount)

        prompt = "Compute new investment [Y/N]? "
        repeat_again = get_yes(prompt)
        if repeat_again == False:
            break


def task3():
    global num_of_jumps
    global m
    m = 1
    
    attempt = 0
    temp = 1

    while attempt < 5:
        attempt += 1
        prompt = "(" + str(temp) + "/5) Enter a number [1-100]: "
        num_input = get_int_input(prompt, 1, 100)
        if num_input == False:
            continue
        if num_input % 2 == 1:
            m = max(m, num_input)
        temp += 1

    num_of_jumps = m
    print("Final max odd number: ", m)


def task4():
    
    prompt = "Press enter to run" + str(m) + "jumping jacks."
    enter = input(prompt)
    for i in range(1, m+1):
    
        frame1 = "  o   [  " + str(i) + "]\n /|\  \n | |  "
        frame2 = " \o/  [  " + str(i) + "]\n  |   \n / \  "
    
        if i % 2 == 0:
            print(frame1)
        else:
            print(frame2)

        time.sleep(0.3)

def main():
    print_student_info()

    print("\n---- Task 1: The Owl ----")
    task1()
    print("\n---- Task 2: Compound investment ---")
    task2()
    print("\n---- Task 3: Max odd number ----")
    task3()
    print("\n---- Task 4: Jumping Jacks ----")
    task4()
    input("Press enter to end lab4!")


if __name__ == "__main__":
    main() 