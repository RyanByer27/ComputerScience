speed = input("Whats the wind speed in MPH\n>")
speed = int(speed)
if speed < 74:
    print("Tropical storm")
elif speed < 96:
    print("Category 1")
elif speed < 111:
    print("Category 2")
elif speed < 130:
    print("Category 3")
elif speed < 157:
    print("Category 4")
elif speed >= 157:
    print("Category 5")