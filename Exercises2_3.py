#Ryan Hutchinson
#1
print("Bon", " Voyage", '!', sep="")

#2
print("Price: ", '$', 23.45, sep="")

#3
print("Portion: ", 90, '%', sep="")

#17
print("NUMBER/tSQUARE")
print(str(2) + "\t" + str(2 ** 2))
print(str(3) + "\t" + str(3 ** 2))

#18
print("COUNTRY\t", "LAND AREA")
print("India\t", 2.5, "million sq km")
print("China\t", 9.6, "million sq km")

#26
print("0123456789")
print("{0:10,d}".format(1234))
print("{0:^10,d}".format(1234))
print("{0:<10,d}".format(1234))

#27
print("${0:,.2f}".format(1234.567))

#30
print("${0:,.2f}".format(1234))

#53
cost = float(input('Enter amount of bill: '))
tip = float(input('Enter percentage tip: '))
tip_calc = (cost * (tip/100))
total_tip = ("Tip: $%.2f" %(tip_calc))
print(total_tip)

#57
principal = float(input('Enter principal: '))
interest = float(input('Enter interest rate (as %): '))
time = float(input('Enter number of years: '))
calc = float(principal * ((1 + (interest / 100))**time))
future_value = ("Future value: $%.2f" %(calc))
print(future_value)
