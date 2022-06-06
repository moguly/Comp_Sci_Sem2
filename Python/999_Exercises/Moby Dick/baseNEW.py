





with open('moby.txt') as f:
   for line in f:
        sentence = line.strip()
        z = len(sentence)
        y = sentence[0:5]
        for i in range (0,len(sentence)):
            whal = ["whale"]
        for i in sentence:             
            if i not in whal:
                whal.append(i) 
        for i in range(0, len(whal)):
         print(whal[i], sentence.count(whal[i]))  
       
f.close()

count = 0

for i in range(0,len(sentence)):
    if sentence[i:i+5]lower == "Whale":
        count = count + 1

print(cout)