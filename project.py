 
 #Data Types
"""age = 90
person_age = input("Enter your age: ")
days = age*365 - int(person_age)*365
weeks = age*52 - int(person_age)*52
months = age*12 - int(person_age)*12
print(f"You have {days} days, {weeks} weeks, and {months} left.")"""
age = int(input("What is your age: "))
year_remaining = 90 - age
days_remaining = year_remaining*365
weeks_remaining = year_remaining*52
months_remaining = year_remaining*12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} left.")
if age>90:
  print("Invalid age")
