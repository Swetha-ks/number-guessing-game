secret = 7
chance = 5
attempts = 0   # count attempts

while chance > 0:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1   # increase attempts

    if guess == secret:
        print("Correct!")
        print("You guessed in", attempts, "attempts")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")

    chance = chance - 1
    print("Chances left:", chance)

if chance == 0:
    print("Game Over!")