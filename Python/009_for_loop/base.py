x = int(input("How long do you want the line to be? "))
y = input("Would you like the line to be Vertical or Horizontal? ")
if y == "Vertical":
    for e in range (0,x):
        print("|")
elif y == "Horizontal":
    for t in range (0,x):
        print("-", end=" ")