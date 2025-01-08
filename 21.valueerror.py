### Question 21: Try-Except for ValueError
'''
**Description:** Handle a ValueError when converting a non-numeric string to an integer.
**Test Case:** For input "abc", the output should be "Invalid input".
'''

try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input")
    
