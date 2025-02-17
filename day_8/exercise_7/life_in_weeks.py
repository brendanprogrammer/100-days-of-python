'''
Life in Weeks
I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

Create a function called life_in_weeks() using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x weeks left.
Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

**Warning** The function must be called life_in_weeks for the tests to pass. Also the output must have the same punctuation and spelling as the example. Including the full stop!

Example Input: 56

Example Output: You have 1768 weeks left.
'''

def life_in_weeks(age):
    remaining_years = 90 - age  # Calculate how many years left to live until 90
    remaining_weeks = remaining_years * 52  # Convert years to weeks (1 year = 52 weeks)
    
    # Output the result with the correct format using an f-string
    print(f"You have {remaining_weeks} weeks left.")
    
# Call the function with hardcoded values for testing
life_in_weeks(56)  # Example call to test the function