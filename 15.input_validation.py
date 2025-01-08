###Question 15: User Input Validation -
'''
Write a Python program that ensures the user enters a valid number. If not, it should prompt again.
Test Case: input = "abc", input = "50"
'''

while True:
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
    
    except:
        print('Invalid input, enter a number', )
    continue
    

    
