x = int(input("What is your first input? "))
z = input("What operation would you like to use? ")
y = int(input("What is your second input? "))
v = x + y
b = x*y
n = x - y
t = x/y


if z == "+":
    print(str(x) + " + " + str(y) + " = " + str(v))
elif z == "*":
    print(str(x) + " * " + str(y) + " = " + str(b))
elif z == "-":
    print(str(x) + " - " + str(y) + " = " + str(n))
elif z == "/":
    print(str(x) + " / " + str(y) + " = " + str(t))
