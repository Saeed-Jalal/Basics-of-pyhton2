#Flow Controls

#if
numbers = 100
if (numbers >=90):
    print("wowwwwwww' you got good marks.")
else:
    print("You passed")
#elif
numbers=90
if (numbers >75):
    print("You have earned first grade.")
elif(numbers>60)and (numbers<=75):
    print("You have earned second grade.")
elif(numbers>45)and (numbers<=60):
    print("You have earned third grade.")
else:
    print("Try again.")


#loops
#while loop
number = 0
while number <8:
    print("Number: ",number)
    number = number+3
print("Code is executed.")

marks=2
while marks <10:
    print("Marks is : ",marks)
    marks = marks +2
print("It is the usage of while loop.")
#Another while loop example
import random
print("What is your name? ")
name = input()
print("Holla! "+ name +", Would you like to guess a number.")
number = 20
guessed = int(number * random.random()) + 1
guess = 0
while guess != guessed:
    guess = int(input("Guess new number:"))
    if guess > 0:
        if guess > guessed:
            print("Your guess is too high.")
        elif guess < guessed:

            print("Your guess is too low.")
    else:
            print("You are not guessing correctly.")
            break
else:
    print("Wowwww! You won.")









