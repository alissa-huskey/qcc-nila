"""this is a Guess the Number Game"""

import random

number=random.randint(1,20)
max_guesses=6

player=input("Hello. What is your name? ")
print("Hello " +player+ ".")
print("I am thinking of a number between 1 and 20.")
print()

for guess_count in range(1,max_guesses):
    print("Guess", guess_count, "of", max_guesses)
    guess=input("Your guess: ")
    guess=int(guess)
    if guess < number:
        print("Your guess is too low.")

    elif guess > number:
        print("Your guess is too high.")

    else:
      break
    print()

if guess == number:
        print("Excellent " + player +" You guessed my number in " + max_count, ".")   

else: 
        number=str(number)
        print("Nope. I was thinking of the number " + number + ".")
    