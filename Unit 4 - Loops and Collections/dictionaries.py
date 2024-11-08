# Dictionary is a type of collection like list
# A lsit is a colelciton of items in a sequence
# A Dictionary is different
# Dictionaries store data in key-value pairs
# You can retreive data quickly by using a unique key
# instead of retreving it by index (position)

#Example
# Lists use brackets, dictionaries use braces
Ryan = {
    "name": "Ryan",
    "age": 15,
    "city": "St. Michael",
    "pets": 2,
    "height": 6.0
}

# Each key must be unique

# Retreiving values from a dictionary
print(Ryan["age"])

# .get allows you to retreive a value without erroring
# when the key doesn't exist
# The second parameter is what is given if value is not found
print(Ryan.get("height"))
print(Ryan.get("weight", "fortnite"))

# You can add values to a dictionary
Ryan["country"] = "USA"

# You can modify values
Ryan["age"] = 2345678

print(Ryan)

# Remove entries
Ryan.pop("pets")

# Iterate through a dictionary using a for loop
for key, value in Ryan.items():
    print(key + ": " + str(value))

# Dictionary functions
print(Ryan.keys())   #returns all keys
print(Ryan.values()) #returns all values
print(Ryan.items())  #returns all pairs
print(Ryan.clear())  #removes all items from the dict