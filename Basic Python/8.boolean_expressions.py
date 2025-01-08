###Question 24: Boolean Expressions
'''
Write a Python program that checks if a number is positive, negative, or zero. Output the result.
Test Case: n = 4, n = -1, n = 0
'''

try:
    n = int(input("Enter a number: "))
    if n == 0:
        print(f'{n} is zero')
    elif n < 0:
        print(f'{n} is negative')
    else:
        print(f'{n} is positive')
except ValueError:
    print('Invalid input. Please enter a valid number.')