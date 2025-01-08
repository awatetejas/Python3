###Question 28: Checking Leap Year
'''
Write a Python program to check whether a given year is a leap year.
Test Case: year = 2000, year = 2021
'''

try:
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        else:
            print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except:
    print("Invalid input. Please enter a valid year.")