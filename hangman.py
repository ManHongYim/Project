import random
import string
from words import words

copy = words['data'][:]
valid_words = []
for word in copy:
    clean_word = word.translate(word.maketrans('','','- '))
    valid_words.append(clean_word)

def hangman(lives=10):
    lives=lives
    random_word = random.choice(valid_words)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(random_word)
    used_letters = set()
    print('Random Gernerated! You can guess it now!')

    while len(word_letters) > 0 and lives>0:
        print('\nLives:',lives)
        print("You have used these words:", ''.join(used_letters))

        current_progress = [letter if letter in used_letters else '_' for letter in random_word]
        print('Current word:', ''.join(current_progress))

        user_input = input('Guess a letter:')
        if user_input == 'quit':break
        try:
            assert len(user_input) == 1 and user_input in string.ascii_letters
        except:
            print('Invalid input, please try again and enter one alphabet letter only!')
            continue
        if user_input not in used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
    if len(word_letters) == 0:
        return print(f'Congrats!, You get the right word! {random_word}')
    if lives == 0:
        return print(f'Lives gone!, Try one more time!',f'The correct word is {random_word}')

hangman()
