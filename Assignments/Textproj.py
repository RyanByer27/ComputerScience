# Weclome to my game in this game there will be 5 paths with 5 difernt endings and 2 hidden endings
# In the game you will be going throug a school day
# A key to navageting the code is #1 is path 1 #2 is path 2 and so on
def Waking_Up():
    print("You Just woke up it is 7am school starts at 8:30 what do you do?")
    print("1. Get up and get ready")#1
    print("2. Get up and go on your phone")#2
    print("3. Go back to bed for an hour")#3
    choice = input(">")
    if choice == 1:
        Geting_ready()
    else:
        print("Invalid Input Try Again")
        Geting_ready()
def Geting_ready():
    print("You got up and ready its now 7:45 what do you do?")
    print("1. Drive To school")#1
    print("2. Ride with a friend to school")#2
    print("3. Go on you phone for a little")#3
    print("4. Fake being sick")#4
    print("5. skip school")#5
    choice2 = input(">")