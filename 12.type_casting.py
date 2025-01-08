###Question 12: Type Casting
'''
Convert a input string "<valid number provide by user>" into an integer and a float, then print their types.
Test Case: "100"
'''

number = input('Enter a number: ')

try:
    int_number = int(number)
    print(int_number)
    print(type(int_number))
    print('-----')
    float_number = float(number)
    print(float_number)
    print(type(float_number))
except ValueError:
    print("Invalid input")