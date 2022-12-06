##################################
# EECS1015 - York University
# Author: Michael S. Brown
# (c) MS Brown. This code cannot be shared without permission from the
# author.
# Lab 7 starter code
##################################

def task0():
    print_student_info()

def is_sorted(a_list):
    blank_list= []
    for num in range(len(a_list) - 1):
        if a_list[num+1]<a_list[num]:
            return False
    return True


def task1():
    x1 = [1, 4, 5, 9, 0, 8, 10]
    x2 = [1, 2, 4, 5, 6, 7, 9]
    x3 = []
    # Write function is_sorted() outside this function
    # apply the function on each list and print the results

    print(is_sorted(x1))
    print(is_sorted(x2))
    print(is_sorted(x3))


# Task 2 fxn
def merge_dict(dict1,dict2):
    for key2 in dict2:
        if key2 not in dict1:
            value2 = dict2[key2]
            dict1.update({key2:value2})
    print("merged dict")


def task2():
    dict1 = {8: "Exercise", 9: "Breakfast", 12: "Lunch", 3: "Study", 6: "Netflix"}
    dict2 = {8: "Sleep", 10: "Lab", 12: "Class", 4: "Call Mom"}
    print("dict1")
    print(dict1)
    print("dict2")
    print(dict2)
    # Write function merge_dict() outside this function
    # print dict1
    # print dict2
    # call merge_dict(dict1, dict2)  <- which will modified dict1
    # print dict1 again (after it is modified)
    merge_dict(dict1,dict2)
    print(dict1)


def invert_dict(a_dict):
    rev_dict = dict()
    for key in a_dict:
        val = a_dict[key]
        rev_dict[val] = key
    return (rev_dict)

def task3():
    a_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    print(a_dict)
    # write function invert_dict() outside this function
    # print a_dict
    # call invert_dict(a_dict)
    # print new dict
    print(invert_dict(a_dict))

def list_to_dict(a_list):
    dict = {}
    print(a_list)
    i = 0
    for items in a_list:
        dict[i] = items
        i += 1
    return dict

def task4():
    my_list = [1, "hello", 9.99, ["EECS", "1015"], {1: "1", 2: "2"}]
    # write function list_to_dict() outside this function
    # print list
    # call list_to_dict(my_list)
    # print new dictionary
    print(list_to_dict(my_list))

def str_list_to_num_list(a_list):
    b_list = []
    for items in a_list:
        y = int(items)
        b_list.append(y)
    print(b_list)

def task5():
    x = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(x)
    # write fucntion str_list_to_num_list()
    # print list x
    # call function str_list_to_num_list(x)
    # print list x again (it should be updated)
    str_list_to_num_list(x)

def merge_list(list1, list2):
    # list 1 and list2 both are sorted
    len1 = len(list1)
    len2 = len(list2)
    index1 = 0
    index2 = 0
    new_list = []
    while index1 < len1 and index2 < len2:
        if (list1[index1] < list2[index2]):
            new_list.append(list1[index1])
            index1 += 1
        else:
            new_list.append(list2[index2])
            index2 += 1

    if len1 > index1:
        new_list.extend(list1[index1:])

    if len2 > index2:
        new_list.extend(list2[index2:])
    return new_list

def task6():
    list1 = (input("Input 1st sorted list of numbers [x1 x2 ...]: ").split(" "))
    list1_int = []
    for item in list1:
        y = int(item)
        list1_int.append(y)
    print(list1_int)

    list2 = (input("Input 2st sorted list of numbers [x1 x2 ...]: ").split(" "))
    list2_int = []
    for items in list2:
        x = int(items)
        list2_int.append(x)
    print(list2_int)
    assert is_sorted(list1_int) , "List 1 is not sorted"
    assert is_sorted(list2_int) , "List 2 is not sorted"
    mergedlist = merge_list(list1_int, list2_int)
    print(mergedlist)

    YN = input("Try again?[Y/N]: ")
    if YN.upper() == 'Y':
        task6()


def main():
    print("\n---- Task 1: Check if list is sorted ----")
    task1()
    print("\n---- Task 2: Merge dictionaries ----")
    task2()
    print("\n---- Task 3: Invert dictionaries ----")
    task3()
    print("\n---- Task 4: List to dictionary ----")
    task4()
    print("\n---- Task 5: String list to num list ----")
    task5()
    print("\n---- Task 6: Merge list with assert ----")
    task6()


if __name__ == "__main__":
    main()
