#Ryan Hutchinson
#5-10
print("Python"[4])
print("Python"[-2])
print("Python"[-3])
print("Python"[5])
print("Python"[0:3])
print("Python"[2:2])

#39
print(len("Grand Hotel"[:6].rstrip()))

#46
print("all clear".title().count('a'))

#47
a = 4
b = 6
c = "Municipality"
d = "pal"
print(len(c))
print(c.upper())
print(c[a:b] + c[b + 4:])
print(c.find(d))

#70
batmanAndRobin= "THE DYNAMIC DUO".lower().title()
print(batmanAndRobin)
      
#82 Indentify Errors
# age = input("Enter your age: ")
# print("Next year you will be " + (age + 1))
print("Error: the input 'age + 1' can not be concatenated because you cannot add a str and int together.")
      
#93
firstName = "Thomas"
middleName = "Alva"
lastName = "Edison"
yearOfBirth = 1847
print(firstName + " " + middleName + " " + lastName + ", " + str(yearOfBirth))
      
#106
cost = float(input('Enter amount of bill: '))
tip = float(input('Enter percentage tip: '))
tip_calc = (cost * (tip/100))
total_tip = ("Tip: $%.2f" %(tip_calc))
print(total_tip)
