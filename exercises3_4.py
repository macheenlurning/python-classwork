# Ryan Hutchinson
# Exercises 3.4

#1
for n in range(7, 11):
    print(n)
    
#2
for n in range(-11, -7):
    print(n)

#9
for n in range(4, 20, 5):
    print(n)

#10
for n in range(0, 4):
    print(n)

#17
for i in range(1,5):
    print("Pass #" + str(i))
    
#18
for i in range(3,7):
    print(2 * i)

#27
word = "183651"
sumOfOddIndexes = 0
oddIndex = False
for ch in word:
    if oddIndex:
        sumOfOddIndexes += int(ch)
    oddIndex = not oddIndex
print(sumOfOddIndexes)        

#28
word = "cloudier"
newWord = ""
evenIndex = True
for ch in word:
    if evenIndex:
        newWord += ch
    evenIndex = not evenIndex
print(newWord)

#36
# I'm looking over a four leaf clover.
leaves = ("sunshine", "rain", "the roses that bloom in the lane",
          "somebody I adore")
number = 1
for leaf in leaves:
    print("Leaf", str(number) + ':', leaf)
    number += 1

#37
# Problem: "assume that the six lines of the file 'Numbers.txt' contain the data 6, 9, 2, 3, 6, 4"
# Changed the initial code to read without errors on your computer - 
# The initial code is commented first, then my code is included below it.

# Original Code
# sumEvens = 0
# infile = open("Numbers.txt", 'r')
# for line in infile:
#     if eval(line) % 2 == 0:
#         sumEvens += eval(line)
#     infile.close()
# print(sumEvens)

#New code
txt = [6, 9, 2, 3, 6, 4]
sumEvens = 0
for n in txt:
    if n % 2 == 0:
        sumEvens += n
print(sumEvens)

#38
# Original Code
# dataList = []
# infile = open("Numbers.txt", 'r')
# for line in infile:
#     dataList.append(eval(line))
# infile.close()
# print(sum(dataList))

# New Code
dataList = []
for n in txt:
    dataList.append(n)
print(sum(dataList))

#41
# for j in range(1, 26, -1):
#     print(j)
print("Problem #41 - Error: cannot count backwards by 1 outside of the range 1-25")

#42
#for i in range(1, 4):
#    print(i + " " + 2 ** i)
print("Problem #42 - Error: unable to concatenate with the '+' for both integers and strings")
      
#52
# Phone Number - write a program that removes the dashes from a telephone number input by the user
tel = input("Enter a telephone number: ")
print("Number without dashes is {}.".format(str(tel.replace('-', ''))))

#53
# Vowels - Count the number of vowels in a phrase input by the user.
phrase = input("Enter a phrase: ")
count = 0
v = ['a', 'A', 'e', 'E',
     'i', 'I', 'o', 'O',
     'u', 'U', 'y', 'Y']
for i in phrase:
    if i in v: count += 1
print("The phrase contains {} vowels.".format(count))
