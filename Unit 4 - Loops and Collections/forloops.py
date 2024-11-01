#for loops
#Big deal
#For loops allow the programer to Repeat or what we call loop

fav_foods = ["Eggs Bennies", "Fried Chicken","Mac n Cheese"]

#for <variabel> in <list>:

for i in range(90,101):
    print(i)

for food in fav_foods:
    print(food)
#runs all of thelines inside of the loop
#when it gets to the bottom of the list it runs again
#and moves onto the next item in the list
#it ends when there are no items left


for n in range(10,0,-1): #Start Stop Step
    print(n)

# sum of a list
numbers = [12, 25, 53, 24, 555]
sum = 0
for num in numbers:
    sum += num
print(sum)


numbers = [1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10]
even_numbers = []

for i in numbers:
    even_numbers.append(i*i)
print(even_numbers)
stringy = input("please enter a string\n")
numvowels = 0
for s in stringy:
    if s.lower() in ["a", "e", "i", "o", "u"]:
        numvowels = numvowels + 1

print(numvowels)

try:
    munti = int(input("INPUNT NOW\n"))
except:
    print("Cry abount it")

for i in range(0,munti+1):
    print(str(munti) + " x " + str(i) + " = " + str(munti*i))


#list of names
names = ["Peter", "John", "Paul", "Luke"]
for names in names:
    print("hello, " + names + "!")
