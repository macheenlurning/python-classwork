# Ryan Hutchinson
# Chapter 3 Exam

# Programming Projects 1 & 3

#1 - Car Loan
loan = int(input("Enter the amount of the loan: "))
if int(loan) >= 100000 or int(loan) < 0:
    print("Total loan value {} might be incorrect...".format(loan))
    response1 = input("Would you like to correct this? Type Yes or No: ").lower()
    if response1 == 'yes':
        loan = int(input("Enter the amount of the loan: "))
    elif response1 == 'no':
        pass
        
annual_rate = float(input("Enter the interest rate: "))
if float(annual_rate) >= 30 or float(annual_rate) < 0:
    print("Annual rate {} might be incorrect?".format(annual_rate))
    response2 = input("Would you like to correct this? Type Yes or No: ").lower()
    if response2 == 'yes':
        annual_rate = float(input("Enter the interest rate: "))
    elif response2 == 'no':
        pass

duration = int(input("Enter the duration in months: "))
if int(duration) > 72 or int(duration) < 12:
    print("Duration of {} months might be incorrect?".format(duration))
    response3 = input("Would you like to correct this? Type Yes or No: ").lower()
    if response3 == 'yes':
        duration = int(input("Enter the duration in months: "))
    elif response3 == 'no':
        pass

monthly_rate = round(((annual_rate/100) / 12), 8)
part1 = round((loan * monthly_rate), 8)
part2 = round(((1 / ((1 + monthly_rate) ** duration))), 8)
part3 = round((1 - part2), 8)

monthly_payment = round(float(part1 / part3), 2)
tot_int = (duration * monthly_payment) - loan

formatted_mp = "{:.2f}".format(monthly_payment)
formatted_ti = "{:.2f}".format(tot_int)
print("Monthly payment: ${}".format(formatted_mp))
print("Total interest paid: ${}".format(formatted_ti))

print()

#3 - Caffeine Absorption
print("CAFFEINE VALUES")

total_caf = 130
hours = 0
while total_caf >= 65:
    total_caf = total_caf * 0.87
    hours += 1
    if total_caf < 65:
        print("One cup: less than 65mg. will remain after {} hours.".format(hours))

total_caf = 130
hours = 0
while hours <25:
    hours += 1
    total_caf = (total_caf * 0.87)
    if hours == 24:
        print("One cup: {:.2f} mg. will remain after 24 hours.".format(total_caf))

total_caf = 130
hours = 0
while hours < 25:
    hours += 1
    total_caf = total_caf * 0.87
    total_caf = total_caf + 130
    if hours == 24:
        print("Hourly cups: {:.2f} mg. will remain after 24 hours.".format(total_caf))




