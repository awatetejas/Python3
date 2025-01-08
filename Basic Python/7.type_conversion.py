### Question 7: Type Conversion (Integer to String)
'''
**Description:** Convert an integer input to a string and concatenate it with another string.
**Test Case:** For input 42 and " is the answer.", the output should be "42 is the answer.".
'''
try:
    num = int(input("Enter an integer: "))
    secondString = input("Enter a string: ")
    result = str(num) + ' ' + secondString
    print(result)
except:
    print("Invalid input. Please enter an integer and a string.")



