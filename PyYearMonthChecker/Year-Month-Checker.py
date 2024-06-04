print("Welcome to python Leap Year checker\n This small program gives you an output if a year is a Leap one and how many days given month has")
print("\n")
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
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month-1]
  

year = int(input("Enter a year to check: ")) 
month = int(input("Enter a month to check for number of days: "))
days = days_in_month(year, month)
if is_leap(year) == True:
  print("\n")
  print(f"The year {year} IS a leap year, and moth {month} has {days} days")
else:
  print(f"The year {year} is NOT a leap year, and moth {month} has {days} days")




