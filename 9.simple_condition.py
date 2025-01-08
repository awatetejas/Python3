### Question 9: Simple Condition
'''
**Description:** Check if a user-provided number is even or odd.
**Test Case:** For input 9, the output should be "Odd".
'''

try:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input. Please enter a valid number.")