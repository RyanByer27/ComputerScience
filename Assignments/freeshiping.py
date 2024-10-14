def free_shipping(prime, cost, age, consent):
    if prime == True or cost >= 25 and age >= 18 or consent == True:
        print("You get FREEEEE shipping!!")
    else:
        print("You dont get free shipping")

free_shipping()