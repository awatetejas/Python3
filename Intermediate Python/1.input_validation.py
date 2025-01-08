### Question 1: Advanced Input Validation
'''
**Description:** Ensure the user inputs an integer within a specified range.
**Test Case:** For input 105 (range: 1-100), the output should include "Input out of range".
'''
def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Input out of range. Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Test the function
if __name__ == "__main__":
    min_range = 1
    max_range = 100
    print(f"Please enter an integer between {min_range} and {max_range}.")
    valid_number = get_valid_input("Enter a number: ", min_range, max_range)
    print(f"You entered a valid number: {valid_number}")        

