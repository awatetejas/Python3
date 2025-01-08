
### Question 18: Input Conversion
'''
**Description:** Convert a string input into a float and display its square.
**Test Case:** For input "3.5", the output should be "Square: 12.25".
'''

try:
    num = float(input("Enter a number: "))
    square = num ** 2
    print(f"Square: {square:.2f}")
except:
    print("Invalid input. Please enter a valid number.")
