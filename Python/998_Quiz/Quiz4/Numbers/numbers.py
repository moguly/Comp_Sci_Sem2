Numbers = [6,9,32,28,15,22,3,18]
highest_number = 0
for number in Numbers:
    if number > highest_number:
        highest_number = number
       
print(highest_number)

Numbers = [6,9,32,28,15,22,3,18]
lowest_number = 100
for number in Numbers:
    if number < lowest_number:
        lowest_number = number
print(lowest_number)

mynumbers = [6,9,32,28,15,22,3,18]
a = 0
 
for i in mynumbers:
     a += i
average = a / float(len(mynumbers))
print(average)