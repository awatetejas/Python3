###Question 14: Conditional Statements with Multiple Conditions
'''
Write a Python program that checks if a number is divisible by both 2 and 3 using multiple conditional statements.
Test Case: n = 6, n = 9, n = 5
'''

try:
    n = int(input("Enter an integer: "))
    if n % 2 == 0 and n % 3 == 0:
        print("The number is divisible by both 2 and 3.")
    elif n % 2 == 0:
        print("The number is divisible by 2 but not 3.")
    elif n % 3 == 0:
        print("The number is divisible by 3 but not 2.")
    else:
        print("The number is not divisible by either 2 or 3.")
except ValueError:
    print("Invalid input. Please enter an integer.")