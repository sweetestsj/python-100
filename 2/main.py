print("Welcome to the tip calculator!")
bill=float(input("how much was the bill?"))
tip=float(input("desired tip percent?"))
people=int(input("how many people?"))

total = bill * (1 + tip/100)
final_amt = round(total/people,2)
print(f"each pay ${final_amt}") 