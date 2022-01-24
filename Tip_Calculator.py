#Calculating Tip Calculator 
print("Welcome to tip calculator!")
bill = float(input("What was the total restaurant bill? $"))
tip = int(input("How much tip would you like to give? 8, 10, 12? "))
people = int(input("How many people to split the restaurant bill?"))
tip_as_percentage = tip / 100 
total_tip = bill * tip_as_percentage
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_bill_amount = round(bill_per_person, 3)
final_bill_amount = "{:.3f}".format(bill_per_person)
print(f"Each person will pay final amount: ${final_bill_amount}")
