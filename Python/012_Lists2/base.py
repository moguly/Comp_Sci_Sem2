import random

x = int(input("How many random numbers would you like? "))
randomlist = random.sample(range(1, 10), x)
print(randomlist)
