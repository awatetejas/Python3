###Question 24: Simple Interest Calculation
'''
Write a Python program to calculate simple interest given principal, rate, and time.
Test Case: principal = 1000, rate = 5, time = 2
'''

try:
    principle = int(input("Enter a principle: "))
    rate = int(input("Enter a rate: "))
    time = int(input("Enter a time: "))
    simple_interest = (principle * rate * time) / 100
    print("Simple Interest is: ", simple_interest)
except:
    print("Invalid input. Please enter a valid number.")