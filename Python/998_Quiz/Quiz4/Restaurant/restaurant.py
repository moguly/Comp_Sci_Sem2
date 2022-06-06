import random 

Thisrestaurant  = ["Mcdonalds","Starbucks","Popeyes"]
MCFoods = ["Big mac", "Mc flurry","Fries"]
Star = ["Grande","Tall","Venti"]
Pop = ["Chicken burger", "Chicken nuggets", "Chicken wrap"]
random_food = random.choice(Thisrestaurant)
print("Random selected restraunt is : " + (random_food))
if(random_food == "Mcdonalds"):
    print(MCFoods)
if(random_food == "Starbucks"):
    print(Star)
if(random_food == "Popeyes"):
    print(Pop)
                                                                                 
