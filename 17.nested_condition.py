### Question 17: Nested Conditions
'''
**Description:** Determine the grade of a student based on a numeric score input.
**Test Case:** For input 85, the output should be "Grade: A".
'''

try:
    score = int(input("Enter your score: "))
    print(score)
    if score >= 90:
        print("You'r Grade is A+" )
    elif score > 85 and score < 90:
        print("You'r Grade is A")
    elif score > 75 and score < 85:
        print("You'r Grade is B")
    elif score > 65 and score < 75:
        print("You'r Grade is C")
    elif score > 55 and score < 65:
        print("You'r Grade is D")
    elif score > 45 and score < 55:
        print("You'r Grade is E")
    else:
        print("You'r Grade is F")
except:
    print("Invalid input")
