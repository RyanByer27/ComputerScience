Q1 = input("whats 2 + 3?\n>")
Q2 = input("Whats 10 X 0\n>")
Q3 = input("Whats 10 - 10 + 5\n>")
Q4 = input("Whats 10 X 10 - 50\n>")
Q5 = input("Whats 90 + 5 - 30\n>")

def tally_score():
    score = 0
    if Q1 == "5":
        score = score + 1
    if Q2 == "0":
        score = score + 1
    if Q3 == "5":
        score = score + 1
    if Q4 == "50":
        score = score + 1
    if Q5 == "65":
        score = score + 1
    print(str(score) + "/5")

tally_score() 