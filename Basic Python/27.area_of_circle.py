###Question 27: Area of a Circle
'''
Write a program to calculate the area of a circle given the radius.
Test Case: radius = 5
'''

try:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14 * (radius ** 2)
    print("Area of Circle: ", area )
except:
    print("Invalid input. Please enter a valid number.")
