#Ryan Hutchinson

states = ["Delaware", "Pennsylvania", "New Jersey",
          "Georgia", "Connecticut", "Massachusetts",
          "Utah", "Oklahoma", "New Mexico",
          "Arizona", "Alaska", "Hawaii"]
#1
print(states[1], states[-1])

#2
print(states[2], states[-2])

#7 -
#print(states.index("Alaska")
print("This answer should be 48 if the full list of states was populated")

#49
print("8 items in the list")

#50
print("9 items in the list")

#59
L = ["sentence", "contains", "five", "words."]
L.insert(0, "This")
print(" ".join (L))
del L[3]
L.insert(3, "six")
L.insert(4, "different")
print(" ".join (L))

#64
list1 = ['h', 'o', 'n', 'P', 'y', 't']
list2 = list1[3:] + list1[:3]
print(("".join(list2)))

#65
tuple1 = ("course", "of", "human", "events", "When", "in", "the")
tuple2 = tuple1[4:] + tuple1[:4]
print((" ".join(tuple2)))

#101
#Write a program that counts the number of words in a sentence input by the user.
sentence = input("Enter a sentence: ")
count = len(sentence.split())
print("Number of words: " + str(count))

