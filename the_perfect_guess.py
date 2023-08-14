import random

number = random.randint(1,100)
attempt=1
guess=int(input("Guess the number: "))

while(True):
     if(guess>number):
        guess=int(input("Guess another number. This one is too big: "))
        attempt+=1

     elif(guess<number):
          guess=int(input("Guess another number. This one is too small: "))
          attempt+=1
          
     else:
        print("Yippeeeee! Your guess is corect. You guessed it right in {attempts} attempts")
        break