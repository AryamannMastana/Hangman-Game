import random
from word_list import choices
from hangman_visuals import lives_visual
import string

def get_random_word(choices):
    word = random.choice(choices)
    return word.upper()

def hangman():
    word = get_random_word(choices)
    word_letters = set(word) # Collects the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # Collection of letters user has guessed

    lives = 7

    # Now we let user give their input
    while len(word_letters) > 0 and lives > 0:
        # Showing and joining letters used
        print('You have', lives, 'lives left and you have used the letters: ', ' '.join(used_letters))

        # Displaying what current word looks like
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(' ')

            else:
                lives = lives - 1 
                print('\nYour letter,', user_letter, 'is not in the word.')
        
        elif user_letter in used_letters:
            print('\nYou have already used that letter, try another one.')
        
        else:
            print('\nThat is not a valid letter.')

    # When len(word_letters) == 0 or lives == 0 we reach here
    if lives == 0:
        print(lives_visual[lives])
        print('You died, game over! The word was', word)
    else:
        print('GG! You guessed the word', word, '!!')

hangman()



