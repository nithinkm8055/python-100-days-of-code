print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_bill_with_tip = bill + (bill * 12/100)
each_person_pays = total_bill_with_tip / people
print(f"Each person pays: {round(each_person_pays,2)}")

