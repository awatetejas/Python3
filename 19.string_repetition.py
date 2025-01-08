### Question 19: String Repetition
'''
**Description:** Take a string and an integer, then repeat the string that many times.
**Test Case:** For inputs "Hi" and 3, the output should be "HiHiHi".
'''

try:
    string = input("Enter a string: ")
    num = int(input("Enter a number: "))
    print(string * num)
except:
    print("Invalid input")  # This will print if the input is not a string or an

