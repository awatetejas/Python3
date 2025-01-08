### Question 16: Error Handling Basics
'''
**Description:** Implement a try-except block to handle division by zero.
**Test Case:** For inputs 5 and 0, the output should be "Cannot divide by zero".
'''
while True:

    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        result = num1 / num2
        print(result)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    continue
