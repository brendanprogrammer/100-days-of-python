# Debug

'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
'''

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:  # Fixed condition (was 4000 before)
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example usage:
print(is_leap(2000))  # True (divisible by 400)
print(is_leap(1900))  # False (divisible by 100 but not 400)
print(is_leap(2024))  # True (divisible by 4 but not 100)
print(is_leap(2023))  # False (not divisible by 4)
