### Question 11: Logical Operators
'''
**Description:** Verify if a number is within the range of 10 to 50 inclusive.
**Test Case:** For input 25, the output should be "Within range".
'''

try:
    num = int(input('Enter a number: '))
    if 10 <= num <= 50:
        print("Within range")
    else:
        print("Out of range")
except:
    print("Invalid input")