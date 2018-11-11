# the purpose of this file is explain conditional statements
def print_desc(func, full_desc, input, output):
    """
    prints the header/description for function
    :param func: function declaration name
    :param full_desc: full description of function
    :param input: array of strings containing each input
    :param output: array of strings containing each output
    :return: None
    """
    print ("*** " + str(func) + " ***")
    print ("Full Description: " + str(full_desc))
    print ("Input: " + str(input))
    print ("Output: " + str(output))
    return None


def explain_if(bool):
    """
    show how the if statement works
    :return: None
    """
    if(bool):
        print("     conditional was true")
    else:
        print("     conditional was false")
    return None


def int_if(int1, int2):
    """
    compare two ints
    :param int1: first int
    :param int2: second int
    :return: bool
    """
    if(int1 < int2):
        print ("        int1 is less that int2")
    if(int1 == int2):
        print("     int1 equals int2")
    else:
            print ("        int1 is greater than int2")
    return None


def value_is_in_list(val, list):
    """
    figure out if a value is in a list
    :param val: value
    :param list: list
    :return:
    """
    if(val in list):
        print("     value is in list")
    else:
        print("     value is not in list")
    return None


print("If statements help make decisions.")

print_desc("explain_if", "this function shows how an if statement works", "bool", "None")
explain_if(True)
print()
print_desc("int_if", "this function compares two itegers", "int1, int2", "None")
int_if(5, 6)
print
print_desc("value_is_in_list", "this function tells you if the value inputted is in the list inputted", "value, list",
           "None")
value_is_in_list(4, [1,2,3,4,5,6])
