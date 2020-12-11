# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?

def oops(my_list):
    for i in range(0, 11):
        print(my_list[i])

def oops(my_dict):
    print(my_dict["d"])

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    oops(my_list)
except IndexError:
    print("That index is not in the list!")


my_dict = {"a":1, "b":2, "c":3}
try:
    oops(my_dict)
except KeyError:
    print("That key does not exist!")
try:
    oops(my_dict)
except IndexError:
    print("That value is not in the list!")
