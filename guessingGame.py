import random

number = random.randint(1,9)
chance = 0

while chance<5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Congratulation!!! YOU WON")
    elif guess<number:
        print("Your guess is too low...Guess a number higer than ",guess)
    else:
        print("Your number is too high...Guess a number lower than",guess)
    chance+=1

    if chance==5:
        print("YOU LOST:( The number is ",number)
