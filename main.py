import random
randNumber = random.randint(1, 101)
print(randNumber)
userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess == randNumber):
        print(f"You Guessed it right! ")
        print(f"You guessed the number in {guesses} guesses.")
    else:
        if(userGuess > randNumber):
            print("You guessed it wrong | Try a smaller number.")
        else:
            print("You guessed it wrong | Try a greater number.")
with open("highscore.txt", 'r') as f:
    highscore = int(f.read())
if(guesses<highscore):
    with open("highscore.txt", 'w') as f:
        f.write(str(guesses))
