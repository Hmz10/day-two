print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the bill? "))
each_person_pay = (bill + (tip/100)*bill)/ people
#total_bill =round(each_person_pay,2)
total_bill = "{:.2f}".format(each_person_pay)
print(f"Each person should pay: ${total_bill}")