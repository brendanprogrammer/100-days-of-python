# Debug

'''
def odd_or_even(number):
    if number % 2 = 0:
        return "This is an even number."
    else:
        return "This is an odd number."
''' 

def odd_or_even(number):
    if number % 2 == 0:  # Fixed '=' to '=='
        return "This is an even number."
    else:
        return "This is an odd number."

# Example usage:
print(odd_or_even(4))   # "This is an even number."
print(odd_or_even(7))   # "This is an odd number."
print(odd_or_even(0))   # "This is an even number."
print(odd_or_even(-3))  # "This is an odd number."
