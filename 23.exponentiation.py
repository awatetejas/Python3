###Question 23: Calculate Power Using Exponentiation
'''
Write a Python program that calculates the result of raising a number to a power.
Test Case: base = 2, exp = 3
'''

try:
    base = int(input("Enter a number: "))
    exp = int(input("Enter the power: "))
    result = base ** exp
    print(f"{base} raised to the power of {exp} is {result}")
except:
    print("Invalid input. Please enter a valid number and power.")