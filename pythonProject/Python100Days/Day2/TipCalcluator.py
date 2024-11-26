print("Welcome to tip Calculator!")
bill = float(input("What was the total bill? Rs: "))
tip = int(input("What percentage would like you to give ? 10, 15,20"))
people = int(input("How many people would like to split"))
tip_as_percent = tip / 100
total_tip_amount = bill + tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: {final_amount}")




