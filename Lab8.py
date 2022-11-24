##################################
# EECS1015 - York University
# Author: Michael S. Brown
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 8 starter code
#
##################################
import random
from random import randint


def print_student_info():
    print("Name: Smith Patel")
    print("Student ID: 219347301")
    print("Section B")
    print("Email: smith04@my.yorku.ca")


# class for task 2
class virus:
    def __init__(self, DNAinput=""):
        if len(DNAinput)==0:
            DNAinput = "".join((random.choice("AGTC")) for i in range(0, 50))
            self.DNA = DNAinput
        else:

            self.DNA = DNAinput

    def getDNA(self):
        return self.DNA

    def replicate(self):
        rand = random.randint(1, 100)
        if rand > 94:
            select = random.randint(0, 49)
            choice = random.choice(['A', 'G', 'T', 'C'])
            mutatedDNA = list(self.DNA)
            mutatedDNA[select] = choice
            mutatedDNA = ''.join(mutatedDNA)
            repli = virus(mutatedDNA)
            return repli
        else:
            return virus(self.DNA)

def find_mutation(virus1, virus2):
    one = list(virus1.getDNA())
    sec = list(virus2.getDNA())
    cmpr = ''
    for i in range(len(one)):
        if one[i] == sec[i]:
            cmpr += ' '
        else:
            cmpr += '^'
    return cmpr


# class for task 1
class lotto_ticket:
    ticket_counter = 1

    def __init__(self):
        self.numbers = set()
        while len(self.numbers) < 5:
            x = randint(1, 20)
            if x not in self.numbers:
                self.numbers.add(x)

        self.ticket_id = lotto_ticket.ticket_counter
        lotto_ticket.ticket_counter += 1

    def print_ticket(self):
        print("Ticket #[  %2d]" % (self.ticket_counter - 1), end=" ")
        for items in self.numbers:
            print(str(items), end="  ")
        print()

    def print_and_return_win(self, lotto_numbers):
        num_matches = 0
        win = (f"Ticket #[  {self.ticket_id:3d}]")
        for item in lotto_numbers:
            if item in self.numbers:
                num_matches += 1
                win += f" *{item:02d}* "
            else:
                win += f" {item:02d} "

        winamt = 0
        if num_matches == 3:
            winamt = 2
        elif num_matches == 4:
            winamt = 20
        elif num_matches == 5:
            winamt = 100

        win += (f" [{num_matches} matches, ${winamt}]")
        print(win)
        return winamt


def task0():
    print_student_info()


def task1():
    def lotto_draw():
        unique_no = set()
        while len(unique_no) < 5:
            x = randint(1, 20)
            if x not in unique_no:
                unique_no.add(x)
        return unique_no

    user_amount = 100
    while True:
        print(f"You have ${user_amount}.")
        no_of_tickets = int(input("How many lotto tickets do you want [$2 each]? "))
        if (no_of_tickets * 2 > user_amount) or (no_of_tickets < 0):
            True
        elif no_of_tickets == 0:
            break
        else:
            user_amount = user_amount - no_of_tickets * 2

            new_list = []
            for i in range(no_of_tickets):
                test = lotto_ticket()
                test.print_ticket()
                new_list.append(test)

            lotto_numbers = lotto_draw()
            print("--LOTTO DRAW--")
            print(f"{lotto_numbers}")

            input("---Press enter to check your winnings---")

            for ticket in new_list:
                win = ticket.print_and_return_win(lotto_numbers)
                user_amount += win
            print(f"THe new amount of the user is ${user_amount}")
            if (user_amount < 2):
                break

    print(f"You have ${user_amount}")


def task2():
    while True:
        name = input('Name of virus: ')
        my_virus = virus()
        original_virus = my_virus
        print('Original DNA sequence: ', my_virus.getDNA())
        n = int(input('How many times to replicate? '))

        for i in range(n):
            my_virus = my_virus.replicate()
            print('Replica [    ' + str(i) + '] DNA sequence = ', my_virus.getDNA())

        print('Comparing latest ' + str(name) + ' virus to the original ' + str(name))
        print(my_virus.getDNA())
        print(original_virus.getDNA())

        cmpr = find_mutation(my_virus, original_virus)
        print(cmpr)

        numberOfmutations = cmpr.count('^')

        if (numberOfmutations == 0):
            print('No mutations detected.')
        elif (numberOfmutations <= 5):
            print(str(numberOfmutations) + ' mutations -- virus is the same')
        else:
            print(str(numberOfmutations) + ' mutations -- a new virus has been created')
        char = input('Do you want to do this again(Y/N): ')
        if char.lower() != 'y':
            break


def main():
    task0()
    print("\n--- Task 1: Lotto LESS Revisited ---")
    task1()
    print("\n--- Task 2: Virus mutator ---")
    task2()


if __name__ == "__main__":
    main()