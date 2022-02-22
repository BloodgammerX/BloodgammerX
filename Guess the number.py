n = 18
print("Guess the number")
guess = 9
print(f"You have {guess} guesses")
while(True):
    inpu = int(input("Write your number: "))
    if guess == 1:
        print("Game over")
        break
    elif inpu > 18:
        print(f"Choose under {inpu}")
        guess = guess - 1
        print(f"You have {guess} guesses left")
        continue
    elif inpu < 18:
        print(f"Chosse over {inpu}")
        guess = guess - 1
        print(f"You have {guess} guesses left")
        continue
    else:
        print("You have won")
        break
# Don't by seeing my code