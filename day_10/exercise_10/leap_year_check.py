def is_leap_year(year):
    # A year is a leap year if it is divisible by 4
    # But if it's also divisible by 100, it must also be divisible by 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Example test cases
print(is_leap_year(2400))  # True
print(is_leap_year(1989))  # False