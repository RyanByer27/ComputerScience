import random
#python has four types of collections
#Tuple
#Ser
#>List
#>Dictioary

#today, were going to focas on litssss
#A list is a way to sotre more that one val in a variable
#the values in the ists are called ITEMS
#ITEMS can be accesd by their INDEX (possiton in the list) indices
#                          0                     1           2                  3            4
best_eldin_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhoud's Fang"]
best_years = [1776, 1985, 1994, 1957, 2016]

print(len(best_eldin_ring_weapons))

print(best_years[1+2])
print(best_eldin_ring_weapons[0])
print(best_eldin_ring_weapons[len(best_eldin_ring_weapons)-1]) #print last item


#list itmes can be chaged
best_eldin_ring_weapons[3] = "Spiked Fist"
print(best_eldin_ring_weapons)

#lsit functions

#.pop()
#remove and index at a given index 
best_eldin_ring_weapons.pop(1) #Remove moonceil form the game

#.remove()
#removes an item by value
best_eldin_ring_weapons.remove("Blasphemous Blade")

#.append()
#adds the value as a new item to the end of the list
best_eldin_ring_weapons.append("Death's Poker")

intrandom = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]
print(intrandom)
#.sort()
#sorts the numbers from smallest to biggest
intrandom.sort
print(intrandom)

#max()
#prints the biggest number in the list
print(max(intrandom))

#min()
#prints the smallest number
print(min(intrandom))

#Strings are just list of charicters :OOO
print(len("Owiski"))