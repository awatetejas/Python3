### Question 22: Boolean Expressions
'''
**Description:** Check if two user inputs are equal and both are greater than 10.
**Test Case:** For inputs 12 and 12, the output should be "Both conditions met".
'''

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if a == b and a > 10 and b > 10:
        print("Both conditions met")
    else:
        print("Conditions not met")
except:
    print("Invalid input")