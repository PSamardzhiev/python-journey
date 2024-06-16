print("Welcome to Python Leap Year Checker\nThis small program gives you an output if a year is a Leap one and how many days a given month has")

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_and_days = {
        "Jan": 31,
        "Feb": 28,
        "Mar": 31,
        "Apr": 30,
        "May": 31,
        "Jun": 30,
        "Jul": 31,
        "Aug": 31,
        "Sep": 30,
        "Oct": 31,
        "Nov": 30,
        "Dec": 31
    }
    if is_leap(year) and month == "Feb":
        return 29
    return month_and_days[month]

# Mapping month numbers to names
month_mapping = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

year = int(input("Enter a year to check: "))
month_input = input("Enter a month (e.g., Jan, Feb, etc. or as a number 1-12) to check for number of days: ")

# Convert month input to appropriate format
if month_input.isdigit():
    month = month_mapping[int(month_input)]
else:
    month = month_input.capitalize()

days = days_in_month(year, month)

if is_leap(year):
    print(f"\nThe year {year} IS a leap year, and month {month} has {days} days")
else:
    print(f"The year {year} is NOT a leap year, and month {month} has {days} days")

