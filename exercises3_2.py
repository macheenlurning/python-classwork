#Ryan Hutchinson
#Exercises 3.2

#1
num = 4
if num <= 9:
    print("Less than ten.")
elif num == 4:
    print("Equal to four.")

#5
a = 5
sentence = ""
if ((3 * a) - 4) < 12:
    sentence = "Remember, "
print(sentence + "tomorrow is another day.")

#7
a = 2
b = 3
c = 5
if (a * b) < c:
    b = 7
else:
    print("Your change contains no dollars.")

#15
# syntax error-
# added parenthesis before the "Enter"
# changed = to ==
# added an "else" clause to the if statement
n = eval((input)("Enter a number: "))
if n == 7:
    print("The square is", n*2)
else:
    print("The negative is", -n)

#16
# syntax error -
# added "number" before < 9
number = 6
if number > 5 and number < 9:
    print("Yes")
else:
    print("No")

#25
# write a program to determine how much to tip the server in a restaurant
# tip should be 15% of the check, with a minimum of $2

bill = float(input("Enter amount of bill: "))
if bill > 2.00:
    print("Tip is ${:.2f}".format(bill * 0.15))

