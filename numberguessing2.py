import random
randomnumber = random.randint(1,100)
def guess(x):
 #   randomnumber = random.randint(1,100)
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
guess(10)
            
def computer_guessing(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low,high)
        feedback = input(f' is {guess} is too high {H}, too low{L}  or if correct guess{C}').lower()
        if feedback == 'h':
            high = guess -1

        elif feedback == 'l':
            low = guess +1

        if guess == randomnumber:
            print("yay you guess a correct number\n")
