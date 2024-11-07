import random
number = random.randint(0,101)
guees = input("Pick a number\n>")
while number != guees:
    if guees == number:
        print("YOU GOT IT!!!!")
    else:
        print("Try again")

print("Done")