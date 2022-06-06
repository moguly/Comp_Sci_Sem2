import random

list_words = []

with open('wordle.txt') as f:
    for line in f:
        l = line.strip()
    list_words.append(l)
    
answers = list_words[random.randrange(2315) ]
a = 0
r = 6
for i in range(0,6) : 
    guess = input ("Guess a 5 letter word: ")
    if answers == guess:
        print("You Win" )
        break
for t in  range(2315) :
    if(guess == list_words[t]):
        a = a + 1
        if(a>0):
            print("Wrong answer" )
        else:
            print("invalid word, guess again")
            r = r+1
        a = 0
    print(answers)
f.close()
