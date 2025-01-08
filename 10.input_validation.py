### Question 10: Input Validation
'''
**Description:** Write a program to ensure the user provides a positive integer as input.
**Test Case:** For input -3, the output should include "Input must be positive".
'''

try:
    num = int(input("Enter a number: "))
    if num <= 0:
        print("Input must be positive")
    else:
        print("Input is valid")
except ValueError:
    print("Invalid input. Please enter a number.")