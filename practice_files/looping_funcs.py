def print_list(some_list):
    """
    prints each value in any given list
    :param some_list: list of something
    :return: nothing, but prints each value in list
    """
    for i in some_list:
        print (i)
    return None

def print_numbers_in_range(lower_bound, upper_bound):
    """
    prints each number within a range
    :param lower_bound: lower bound of range
    :param upper_bound: upper bound of range
    :return: none
    """
    range = range(lower_bound, upper_bound)
    for i in range:
        print (i)
    return None


def find_sum(int_list):
    """
    this function adds all the integers in an array together and returns the sum
    :param int_list: list of ints
    :return: sum of all ints in array
    """
    sum = 0
    for i in int_list:
        sum = sum + i
    return sum


def print_index_of_val(some_list, val_in_list):
    """
    this function loops through the list until it finds that val it is looking for, then it prints its idex
    :param some_list: list of anything
    :param val_in_list: value in this list of anything
    :return: index of desired val
    """
    found = False
    index = 0
    while(found == False):
        if(some_list[index] == val_in_list):
            found = True
        else:
            index = index + 1
    return index





intro_messege = "The purpose of this program is to give you examples of things you can do with the loops we've\n" \
                + "learned about. Take the code line by line and notice the outputs. These loops are [for each,\n" \
                + "while, and for in range].\n"
for_each_loop = "A for each loop loops through every value in an array."
while_loop = "A while loop loops through until some condition is met or broken."
range_loop = "A for in range loop denotes a value and loops over this value for all values in the specified range.\n" \
             "* It is important to note that the range is lower bound inclusive and upper bound exclusive\n" \
             "range(1, 5) = [1, 2, 3, 4]"
print ("\n")
print ("\n")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print intro_messege
print("The follwoing list that will be used in the examples is as follows:\nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n")

print for_each_loop
print ("Function: print_list\nInput: list\nReturn: None")
print_list(list)
print ("\n")

print while_loop
print ("Function: print_index_of_val\nInput: list, val_in_list = 3\nReturn: index where value is found")
print("Value Returned = " + str(print_index_of_val(list, 3)))
print ("\n")

print range_loop
print ("Function: print_numbers_in_range\nInput: lower_bound = 5, upper_bound = 15\nReturn: None")
print_numbers_in_range(5, 15)

