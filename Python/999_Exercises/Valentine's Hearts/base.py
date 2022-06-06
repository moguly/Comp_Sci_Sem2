import datetime

people_list = []

with open('People.txt') as f:
    for line in f:
        l = line.strip()
        people_list.append(l)
    

compliment_list = []
with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        compliment_list.append(l)

import random
pnum = random.randrange(0,len(people_list))
cnum = random.randrange(0,len(compliment_list))

print(people_list[pnum] + " " + compliment_list[cnum])

x = datetime.datetime.now()
while(x.minute != 07):
    x = datetime.datetime.now()
    print("It's " + str(x.minute) + " at " + str(x.second) + " seconds ")
    

print()
print("The date and time are:")
print(str(x.day) + "/" + str(x.month) + "/" + str(x.year) + " at " + str(x.hour))

f.close()
