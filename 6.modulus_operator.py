### Question 6: Modulus Operator
'''
**Description:** Write a program to compute the remainder of a division operation.
**Test Case:** For inputs 17 and 5, the output should be "Remainder: 2".
'''

try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    print('')
    print('a:',a)
    print('b:',b)
    print('')

    remainder = a % b
    print('Remainder:',remainder)
except ValueError:
    print("Invalid input. Please enter a valid number.")