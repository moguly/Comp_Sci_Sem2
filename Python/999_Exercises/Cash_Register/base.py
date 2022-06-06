x = int(input("How many items would you like to be purchasing? "))

total = 0
for i in range (0,x):
    y = input("What items are you purchasing? ")
    z = float(input("How much is the item? "))
    print("Thank you for purchasing " + y + "! " )
    total = total + z

print("Your total is: " + str(total))



