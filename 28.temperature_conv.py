###Question 28: Convert Fahrenheit to Celsius
'''
Write a program that converts a given temperature in Fahrenheit to Celsius.
Test Case: temp = 98.6
'''

try:
    # Get the temperature in Fahrenheit from the user
    temp = float(input("Enter the temperature in Fahrenheit: "))
    fah_to_cels = (temp - 32) / 1.8
    print(f"The temperature in Celsius is {fah_to_cels:.2f}")
except:
    print("Invalid input. Please enter a valid temperature in Fahrenheit.")

