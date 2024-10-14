age = input("how old are you?\n>")
exp = input("How many years of experace do you have\n>")

def cheak_elegabilty(age, exp):
    if age >= 18 and exp >= 1:
        print("You are eligible!")

    else:
        print("You are NOT eligible")

cheak_elegabilty()