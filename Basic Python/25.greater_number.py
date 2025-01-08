###Question 25: Check for Greater Number
'''
Write a Python program to find the larger of two numbers.
Test Case: a = 5, b = 10
'''

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
except:
    print("Invalid input. Please enter a valid number.")
