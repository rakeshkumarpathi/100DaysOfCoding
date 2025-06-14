print("Welcome to the tip calculator!")
total_bill = float(input("what was the total bill? $"))
tip_percentage = int(input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * (tip_percentage / 100)
total_bill_with_tip = total_bill + tip
bill_per_person = total_bill_with_tip / people
total_bill_with_tip_per_person = round(bill_per_person, 2)
print(f"Each person should pay: ${total_bill_with_tip_per_person}")