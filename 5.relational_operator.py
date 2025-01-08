### Question 5: Relational Operators
'''
**Description:** Determine if one number is greater than, less than, or equal to another number.
**Test Case:** For inputs 5 and 10, output should include "5 is less than 10".
'''
try:

    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))

    if a == b:
        print(f'{a} is equal to {b}.')
    elif a < b:
        print(f'{a} is less than {b}.')
    else:
        print(f'{a} is greater than {b}.')

except:
    print("Invalid input. Please enter a valid number.")
    

