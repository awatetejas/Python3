### Question 1: Advanced Input Validation
'''
**Description:** Ensure the user inputs an integer within a specified range.
**Test Case:** For input 105 (range: 1-100), the output should include "Input out of range".
'''
try:
    num = int(input("Enter a number between 1 and 100: "))
except:
    print("Invalid input. Please enter an integer.")

for i in range(1,100):
    if num < 1 or num > 100:
        print("Input out of range")
    else:
        print("Input is within the specified range")
        

