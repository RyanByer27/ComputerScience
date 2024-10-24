# Weclome to my game in this game there will be 5 paths with 5 difernt endings and 2 hidden endings
# In the game you will be going through a school day
# A key to navageting the code is #1 is path 1 #2 is path 2 and so on
def Waking_Up():#Start
    print("You Just woke up it is 7am school starts at 8:30 what do you do?")
    print("1. Get up and get ready")# Line 
    print("2. Get up and go on your phone")# line 
    print("3. Go back to bed for an hour")# line
    choice = input(">")
    if choice == "1":
        Geting_ready()
    elif choice == "2":
        Go_on_Phone()
    elif choice == "3":
        Go_to_bed()
    else:
        print("Invalid Input Try Again")
        Waking_Up()

def Geting_ready():#path 1
    print("You got up and ready its now 7:45 what do you do?")
    print("1. Drive To school")
    print("2. Eat Brakfast")
    print("3. Go on you phone for a little")
    print("4. Fake being sick")
    print("5. skip school")
    choice2 = input(">")
    if choice2 == "1":
        DriveToSchool()

def Go_on_Phone():#path 2
    print("You just watched a funny tiktok and now you look at the time and its 8 what do you do?")
    print("1. Go back on your phone")
    print("2. Get ready")
    choice3 = input(">")

def Go_to_bed():
    print("You just woke up and its 8:40 what to you do?")
    print("1. Get ready and speed to school")
    print("2. Just get ready slowly and go")
    print("3. Skip school")
    choice4 = input(">")

def DriveToSchool():
    print("You got to school at 8 what do you do know")
    print("1. Go to home room")
    print("2. Eat brekfast")
    print("3. Go find your friend")
    choice5 = input(">")

def eatbrekfast():
    print("You just got done eating and it is 8 what do you do now?")
    print("1. Go to school")
    print("2. Play fortnite")

Waking_Up()