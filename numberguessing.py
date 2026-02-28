import random
def guess(x):
    randomnumber = random.randint(1,100)
    guess = 0
    print("Welcome to a number guessing game \n")
    while guess != randomnumber:
        guess = int(input(f"guess the correct number\n"))
        if guess < randomnumber:
            print("guess a larger  number")
        elif guess > randomnumber:
            print("guess a smaller number")
        if guess == randomnumber:
            print("yay you guess a correct number\n")
    
guess(100)