################################
# EECS1015, York University
# Lab 5 starting code
# Name:  Smith Patel
# Section: B
# Student ID: 219347301
# Email:  smith04@my.yorku.ca
################################

import random


# Print info
def print_lab_info():
    print("---- Lab 5 ----")
    print("Name: Smith Patel")
    print("Section B")
    print("Student id: 219347301")
    print("Email: smith04@my.yorku.ca")


def task0():
    # Example of calling a function from taskX() functions.
    # you should write all functions "outside" your task1()-task4() functions.
    print_lab_info()


def task1():
    while True:
        def input_list():
            list = []
            i = 0
            while i >= 0:
                i = float(input("Enter the number:"))
                if i >= 0:
                    list.append(i)
            return list

        def compute_avg(aList):
            sum1 = sum(aList)
            num_of_term = len(aList)
            if sum1 == 0:
                print("The sum is 0.00")
            else:
                print(f"List average: {sum1 / num_of_term:.2f}")

        list1 = input_list()
        compute_avg(list1)

        do_again = input("Enter Y or N").upper()
        if do_again == "N":
            break


def task2():
    prompt = input("Input a long String: ").upper()

    plist = list(prompt)
    pset = set(prompt)
    myDict = {}

    x = myDict.fromkeys(pset, 0)

    for key in plist:
        x[key] = x[key] + 1

    for keys in x:
        print(f"'{keys}' |" + "*" * x[keys])


def task3():
    encoder = {'A': '$', 'B': 'F', 'C': 'C', 'D': '2', 'E': 'B', 'F': 'I', 'G': '=', 'H': '*', 'I': '"', 'J': ']',
               'K': '1',
               'L': '0', 'M': '@', 'N': '[', 'O': 'L', 'P': '%', 'Q': '&', 'R': '(', 'S': 'G', 'T': 'K', 'U': '5',
               'V': '!',
               'W': '^', 'X': '+', 'Y': '6', 'Z': '-', '1': 'H', '2': 'A', '3': 'J', '4': '7', '5': '4', '6': 'D',
               '7': 'E',
               '8': '9', '9': ')', '0': ';', ',': '3', '.': '/', ' ': '_'}
    decoder = {'$': 'A', 'F': 'B', 'C': 'C', '2': 'D', 'B': 'E', 'I': 'F', '=': 'G', '*': 'H', '"': 'I', ']': 'J',
               '1': 'K',
               '0': 'L', '@': 'M', '[': 'N', 'L': 'O', '%': 'P', '&': 'Q', '(': 'R', 'G': 'S', 'K': 'T', '5': 'U',
               '!': 'V',
               '^': 'W', '+': 'X', '6': 'Y', '-': 'Z', 'H': '1', 'A': '2', 'J': '3', '7': '4', '4': '5', 'D': '6',
               'E': '7',
               '9': '8', ')': '9', ';': '0', '3': ',', '/': '.', '_': ' '}
    i = 0
    while (i == 0):
        prompt = input("Input Message: ").upper()

        En_De = input("Encode (E) or Decode (D)?").upper()
        a = list(prompt)
        if En_De == "E":
            for keys in a:
                print(encoder[keys], end="")
        elif En_De == "D":
            for keys in a:
                print(decoder[keys], end="")

        do_again = input("\nEnter Y/N").upper()
        if do_again == "Y":
            i = 0
        elif do_again == "N":
            i = 1


def task4():
    while True:
        def random_set():
            s = set()
            while len(s) < 5:
                s.add((random.randint(1, 20)))
            return s

        def print_set(aSet, prompt=""):
            c = 0
            user_input = input(prompt).split(" ")
            aSet = set(user_input)
            while not(len(aSet) == 5):
                user_input = input(prompt).split(" ")
                aSet = set(user_input)

            computer_set = random_set()
            print("Computer's Numbers: ", end="")
            for items in computer_set:
                print(items, end=" ")
            print()

            match_set = set()
            for i in aSet:
                for items in computer_set:
                    if str(i) == str(items):
                        c += 1
                        match_set.add(i)

            if c != 0:
                print(f"{c} matches found: ", end=" ")
                for values in match_set:
                    print(values, end=" ")
            else:
                print("NO MATCHES !!", end="")
            # calling the functions

        print_set(0, "Enter 5 numbers between 1-20: ")
        play_again = input("\nTry again [Y/N]?").upper()
        if play_again == "Y":
            True
        elif play_again == "N":
            break


def main():
    ### Don't forget to update print_lab_info() function
    task0()

    print("\n---- Task 1: List average ----")
    task1()

    print("\n---- Task 2: Character count graph ----")
    task2()

    print("\n---- Task 3: Encoder/decoder ----")
    task3()

    print("\n---- Task 4: Lotto LESS ----")
    task4()


if __name__ == "__main__":
    main()