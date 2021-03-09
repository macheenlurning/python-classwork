# Ryan Hutchinson
# Exam 1

print("Project 1")
total_change = int(input("Enter amount of change: "))
quarters = int(total_change / 25)
dimes = int((total_change - (quarters * 25)) / 10)
nickels = int(((total_change - (quarters * 25) - (dimes * 10)) / 5))
cents = int((total_change - (quarters * 25) - (dimes * 10) - (nickels * 5)))
print("Quarters: " + str(quarters),
      "\tDimes: " + str(dimes))
print("Nickels: " + str(nickels),
      "\tCents: " + str(cents))
print()

print("Project 2")
loan = float(input("Enter amount of loan: "))
rate = float(input("Enter interest rate (%): "))
time = float(input("Enter number of years: "))
payment = float(((rate/1200) / (1-((1+(rate/1200))**(-12 * time)))) * loan)
print("Monthly payment: $%.2f" %payment)
