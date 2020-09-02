import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"
attempts = 10
selected = random.randint(1,100)
bingo = False

for i in range(attempts):
    if attempts > 0 and bingo == False:
        print("You have " + str(attempts) + " attempts left.")
        guess = input("Guess a number between 0 and 100: ")
        if int(guess) == selected:
            bingo = True
            print(" Congrats! You picked the right number!")
        else:
            attempts -= 1
            if attempts != 0:
                print("Wrong. Try again!")
            else:
                print("You lose. The number was " + str(selected) +".")
