
def divide_two_numbers():
    try:
        x  = int(input("What is the first number?\n>"))
        y  = int(input("What is the second number?\n>"))

    except ZeroDivisionError:
        print("cannot dvive by zero, try again.")
        divide_two_numbers()
        
    except:
        print("invalid input, try again.")
        divide_two_numbers()


divide_two_numbers()
