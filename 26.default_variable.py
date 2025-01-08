### Question 26: Default Variables
'''
**Description:** Use default values for variables if no input is provided.
**Test Case:** For no input, the program should use the default value and print it.
'''
a = 10
b = 20

a = input("Enter a value for a: ") or a
b = input("Enter a value for b: ") or b

try:
    print("a =", a)
    print("b =", b)
except:
    print(a)
    print(b)

    


