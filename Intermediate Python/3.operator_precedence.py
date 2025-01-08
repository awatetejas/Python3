### Question 3: Operator Precedence
'''
**Description:** Evaluate a complex expression combining arithmetic and logical operators.
**Test Case:** For inputs `x=4, y=2`, compute `x**2 + 3*y > 10`.
'''

try:
    x = int(input("Enter a first number: "))
    y  = int(input("Enter a second number: "))
    result = (x**2 + 3*y) > 10
    print(result)
except:
    print("Invalid input")
