import random 
print("NUMBER GUESSING GAME")
number=random.randint(1,9)
chances=0
print("GUESS A NUMBER BETWEEN 1 AND 9")
while(chances<5):
    Guess=int(input("Enter your number"))
    if Guess==number:
        print("Congrulation, YOU WON")
        break
    elif Guess<number:
        print("Your guess was too low ")
    else:
        print("Your guess was too high")
    chances=chances+1
if not chances<5:
    print("you loss")