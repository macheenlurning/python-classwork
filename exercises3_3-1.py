# Ryan Hutchinson
# Exercises 3.3

#1
num = 3
while True:
    num = 2 * num
    if num > 15:
        break
    print(num)

#5
list1 = [2, 4, 6, 8]
total = 0
while list1: #same as while list1 != []
    total += list1[0]
    list1 = list1[1:]
print(total)

#7
list1 = ['a', 'b', 'c', 'd']
i = 0
while True:
    print(list1[i])
    i += 1
    if i == len(list1):
        break

#9
# error: this would result in an infinite loop
# added "break" to end loop
# also added () around computation for visibility / syntax
q = 1
while q > 0:
    q = (3 * q) - 1
    print(q)
    break

#10
# Original Code below: multiple syntax errors and infinite loop

## display the numbers 1 through 5
##num = 0
##while True:
##    num = 1
##    print(num)
##    num += 1

# MY CORRECTIONS: added ':' to properly begin while statement,
# moved the 'num += 1' at the front of the statement to start at 1
# added an if statement to show where code should stop,
# added a break to end loop

# display the numbers 1 through 5
num = 0
while True:
    num += 1
    print(num)
    if num == 5:
        break

#13
three_names = 0
while True:
    name = input("Enter a name: ")
    print(name)
    three_names += 1
    if three_names == 3:
        break

#15
# Write a program that displays a Celsius - Fahrenheit conversion table
# Entries in the table should range from 10 to 30 degrees Celsius
# in increments of 5 degrees.

celsius = [10, 15, 20, 25, 30]
fahrenheit = []
for c in celsius:
    f = (((9/5) * c) + 32)
    fahrenheit.append(f)
print("{0:<10s}{1:>3s}".format('Celsius','Fahrenheit'))
numb = 0
while numb < 5:
    print('{0:}{1:10}'.format(celsius[numb],int(fahrenheit[numb])))
    numb += 1
    
    
