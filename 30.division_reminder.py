###Question 30: Find Remainder of Division
'''
Write a program that finds the remainder when one number is divided by another.
Test Case: a = 10, b = 3
'''

try:
    a = int(input("Enter a number1: "))
    b = int(input("Enter a number2: "))
    remainder = a % b
    print(f"The remainder of {a} divided by {b} is {remainder}")
except:
    print("Invalid input. Please enter a valid number.")