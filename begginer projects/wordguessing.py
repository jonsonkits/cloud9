import random

#words used for the guessing game
words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics', 'player',
	'condition', 'reverse', 'water', 'board', 'geeks']

#choose a random word
word = random.choice(words)

print("\t\t\tguess the characters")
guesses = ''

#number of turns to play the game
turns = 12

#repetitive guessing
while turns > 0:
    #number of times the user fails
    failed = 0
    
    #guessing the characters of the word
    for char in word:
        #comparing chaaracters in chosed words with guessed character
        if char in guesses:
            print(char, end="")
            
        else:
            print("_")
            #increment the number of failures
    failed =+ 1
            
    #guessing right
    if failed == 0:
        print("you have won the game")
        print("the magic word is: ", word)
        break
    
    guess = input("guess a character: ")
    guesses += guess
    
    #if guessed character not in word
    if guess not in word:
        turns -= 1
        print("wrong guess")
        
        #the number of turns left
        print("you have ", turns, "more guesses left")
        
        #running out of guesses
        if turns == 0:
            print("you loose")
