print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = total_bill * tip_as_percent
total_bill_with_tip = total_bill + total_tip_amount
bill_per_person = total_bill_with_tip / people
final_amount = round(bill_per_person, 2)
final_amount_as_string = str(final_amount)

print(f"Each person should pay: ${final_amount_as_string}")
