# Task 2
# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values given by the input function were not numbers, 
# and if value b was zero (cannot divide by zero).    

try:
    a = (int (input("Enter your number a :")))
    b = (int (input("Enter your number b :")))
    print ((a / b) * (a / b))
except (ValueError, TypeError):
    print("Please enter the number(integer or float)")
except ZeroDivisionError:
    print("Unfortunately, you cannot divide by zero")
    