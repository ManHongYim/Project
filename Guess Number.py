import random

print('Now, we want to play a guessing game, you need to input a lower bound and upper bound for the number, and you will guess it!')

lower_bound = int(input('Enter a lower bound:'))
upper_bound = int(input('Enter a upper bound:'))

random_number = random.randint(lower_bound,upper_bound)
print(f'Computer already generated a random number between {lower_bound}-{upper_bound}, please input a number to guess it!!')
while True:
    guess = input('Guess a number:')
    if guess == 'quit': break
    try:
        assert int(guess) in range(lower_bound, upper_bound + 1)
    except:
        print(f'Please enter a valid number between {lower_bound}-{upper_bound}!')
        continue #return to the start of loop

    if int(guess) < random_number:
        try:
            assert int(guess) in range(lower_bound, upper_bound + 1)
            lower_bound = int(guess)
            print(f"Now the range changed from {lower_bound} to {upper_bound}")
            continue
        except:
            print(f'Please enter a valid number between {lower_bound}-{upper_bound}!')
            continue
    elif int(guess) > random_number:
        try:
            assert int(guess) in range(lower_bound, upper_bound + 1)
            upper_bound = int(guess)
            print(f"Now the range changed from {lower_bound} to {upper_bound}")
            continue
        except:
            print(f'Please enter a valid number between {lower_bound}-{upper_bound}!')
            continue
    elif int(guess) == random_number:
        print(f"Yes, You got the right number {int(guess)}!")
        break

