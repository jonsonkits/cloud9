import random
import math

#get the upper and lower bounds
lower = int(input("please input the lower bounds of your range: "))
upper = int(input("please input the upper bounds of your range: "))

#create the random range based on your input
x = random.randint(lower, upper)

#use log to culculate the number of guesses permissible
print("\n\tYou have ", round(math.log(upper-lower + 1, 2)), "chances to guess the correct number.\n")

#initialise the number of guesses
count = 0

#make repetitive guessing
while count < math.log(upper - lower + 1, 2):
    count += 1
    
    #take user input
    guess = int(input("input your guess: "))
    
    #test conditions
    if x == guess:
        print("congratulation you guessed right, you made ", count, "try")
        break
    elif x < guess:
        print("your guess is a high number, go lower")
    elif x > guess:
        print("your guess is is a low number, go higher")
        
if count >= math.log(upper -lower + 1, 2):
    print("the correct number is %d" , x)
    print("try again you lost")