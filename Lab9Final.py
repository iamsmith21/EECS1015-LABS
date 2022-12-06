###########################################
# EECS1015 - Practice Final Exam
# Fall 2022, York University
# Starting code
#
###########################################
import random

def task0():
    student_info()

def task1():
    while True:
        myStr = input("Type in a long sentence: ").split(" ")

        removeItem = input("Remove words containing: ")
        with_substring = []
        c = ''
        for item in myStr:
            if removeItem in item:
                with_substring.append(item)
                c = " ".join(with_substring)
        print(f"With substring: '{c}'")

        without_substring = []
        for item in myStr:
            c = ''
            if removeItem not in item:
                without_substring.append(item)
                wc = " ".join(without_substring)
        print(f"W/O substring: '{wc}'")

        tA = input("Do you want to Try Again [Y/N]").upper()
        if tA == "Y":
            True
        else:
            break

# write randomlist and reshape for task2 below
def random_list(N):
    myList = []
    for i in range(N):
        m = random.randint(0,9)
        myList.append(m)
    return myList

def reshape(alist, num_rows, num_cols):
    final_list = []
    a = 0
    for i in range(0,num_rows):
        nestedlist = []
        for j in range(0,num_cols):
            newlist = alist[a]
            nestedlist.append(newlist)
            a+=1
        final_list.append(nestedlist)
    return final_list

def task2():
    while True:
        N = int(input("List length: "))
        randList = random_list(N)
        print(randList)
        numRows = int(input("Rows: "))
        numCols = int(input("Cols: "))

        while numRows*numCols != N:
            print(f"Error: {numRows}*{numCols} != {N}")
            numRows = int(input("Rows: "))
            numCols = int(input("Cols: "))
        else:
            print(reshape(randList,numRows,numCols))

        dA = input("Try Again [Y/N] ").upper()
        if dA == "Y":
            True
        else:
            break

# write function find_duplicates() for task 3 below
def find_diplicates(a_dict):
    empty_Dict = {}
    for items in a_dict:
        empty_Dict[a_dict[items]] = []
# Empty Dict : {'This': [], 'is': [], 'only': [], 'a': [], 'test': [], 'has': [], 'always': [], 'been': []}
# a_dict = {1: 'This', 2: 'is', 3: 'only', 4: 'a', 5: 'test', 6: 'This', 7: 'test', 8: 'has', 9: 'always',
    # 10: 'been', 11: 'a', 12: 'test'}
    final_dict = {}
    for i in empty_Dict:
        final_list = []
        for j in a_dict:
            if i == a_dict[j]:
                final_list.append(j)
        if len(final_list) >=2:
            final_dict[i] = final_list

    return final_dict

def task3():
    while True:
        a_dict = {}
        input("Input words, press enter to end.")
        c = 1
        user_input= 0
        while user_input!='':
            user_input = input(f"[Input {c}] Word: ")
            if user_input!="":
                a_dict[c] = user_input
            c+=1
        print("Dictionary")
        print(a_dict)

        print("Duplicates")
        print(find_diplicates(a_dict))

        dA = input("Try Again? ").upper()
        if dA != "Y":
            break

# write class rangeChecker for task4 below
class rangeChecker:
    range_counter = 1

    def __init__(self,name,min_value,max_value):
        assert max_value > min_value, "max is not max"
        self.id = rangeChecker.range_counter
        rangeChecker.range_counter +=1
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def within_range(self,number):

        if self.min_value <= number <= self.max_value:
            return True
        else:
            return False

    def outside_range(self,number):

        if number < self.min_value or number > self.max_value:
            return True
        else:
            return False

    def print(self):
        print(f"rangeChecker  [{self.id:2d}] '{self.name:10s}' -  {self.min_value:8.2f} <= num <= {self.max_value:8.2f}")

def task4():
    while True:
        newList = []
        print("Input three range checker object")

        for i in range(3):#1, 2
            name,min_value,max_value = input(f"Range {i} Name,Min,Max").split(",")
            min_value = float(min_value)
            max_value = float(max_value)

            callClass = rangeChecker(name,min_value,max_value) #3
            newList.append(callClass)

        input_list = input("Input list of numbers x1,x2,..,xn:").split(",")#4
        num_list = []
        for i in input_list:
            i = float(i)
            num_list.append(i)

        for item in newList:
            item.print()
            for i in num_list:
                within = item.within_range(i)
                print(f"Inside Range: [{i:.2f}]: {within}")

        for item in newList:
            item.print()
            for i in num_list:
                outside = item.outside_range(i)
                print(f"Outside Range: [{i:.2f}]: {outside}")
            print()

        dA = input("Try Again? ").upper()
        if dA != "Y":
            break

def main():
    print("--- Task 1 ---")
    task1()
    print("\n--- Task 2 ---")
    task2()
    print("\n--- Task 3 ---")
    task3()
    print("\n--- Task 4 ---")
    task4()

if __name__ == "__main__":
    main()