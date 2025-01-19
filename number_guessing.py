import random
target = random.randint(1,10)

while True:
    guess = int(input('Enter Your Guess : '))
    if(guess == target):
        print('Success.')
        break
    elif(guess < target):
        print('Too Low Guess!')
    elif(guess > target):
        print('Too High Guess!')
    else:
        print('Invalid')