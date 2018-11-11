# the purpose of this file is give you practice with lists and working with them
#   I will show you a handful of useful functions that can be called on a list


# def len(list):
#     count = 0
#     for i in list:
#         count = count + 1
#
#     return count


# overview
print
print
print ("********* The following functions are called on list objects *********")
print
print

my_list = [1, 2, 3, 4]

# len
print "To find the length of a list, use the len() function."
print "my_list = " + str(my_list)
print "len(my_list) = " + str(len(my_list))
print
print

# append
print "The .append() function adds a value to the end of a list."
print "Original list: my_list = " + str(my_list)
print "... my_list.append(5) ..."
my_list.append(5)
print "Appended list: my_list = " + str(my_list)
print
print

# remove
print "The .remove() funciton acts similarly to the .append() function."
print "Original list: my_list = " + str(my_list)
print "... my_list.remove(2) ..."
my_list.remove(2)
print "Item removed from list: my_list = " + str(my_list)
print
print


# remove
my_list = [8, 4, 5, 3, 1]
print "Original list: my_list = " + str(my_list)
print "... my_list.pop(1) ..."
my_list.pop(1)
print "Item removed from list: my_list = " + str(my_list)
print
print


# sort
my_list = [8, 2, 4, 1, 7, 5]
print "The .sort() function sorts the list."
print "Original list: my_list = " + str(my_list)
print "... my_list.sort() ..."
my_list.sort()
print "Sorted list: my_list = " + str(my_list)
print
print


# sort
print "The .reverse() function reverses the order of the elements in the list."
print "Original list: my_list = " + str(my_list)
print "... my_list.reverse() ..."
my_list.reverse()
print "Sorted list: my_list = " + str(my_list)
print
print

# extend
list2 = [11, 22, 33, 44]
print "The .extend() function combines two list by adding one onto the end - make sure you understand how \nthe lists are combined!"
print "Original list: my_list = " + str(my_list)
print "     list to be combined: list2 = [11, 22, 33, 44]"
print "... my_list.extend(list2) ...           NOTE: notice what is being passed into the function."
my_list.extend(list2)
print "Combined list: my_list = " + str(my_list)
print
print

# count
my_list = [1, 1, 1, 2, 3, 4]
print "The .count() function counts the the number of times a specific element is in the list - understand what is \nbeing passed into the function.."
print "my_list = " + str(my_list)
print "my_list.count(2) = " + str(my_list.count(2))
print "my_list.count(1) = " + str(my_list.count(1))
print
print



my_list = [1,2,3,4,5]
for i in my_list:
    i = i + 1
print my_list