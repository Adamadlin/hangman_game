import word_db 
import drawings
import random


# pre written random world selection 
random_animal = random.choice(word_db.animals_list).strip().lower()
random_car = random.choice(word_db.car_brands_list).strip().lower()
random_musician = random.choice(word_db.musicians_list).strip().lower()


print("\n-------------Welcome to Hangman-------------\n")
subject= int(input('please choose a topic 1 animals ,2-cars,3-musicians'))
difficulty = int(input('please choose a difficulty 1-easy,2-meduim,3-hard'))


# hanlde which subject to display depending on user choise 
def get_word():
    if subject==1:
        return random_animal
    if subject ==2:
        return random_car
    if subject ==3:
        return random_musician
    

# validating the cooect difficulty level from the user 
def handle_difficulty():
    if difficulty in [1, 2, 3]:
                return difficulty
    else:
        print("Invalid input. Please enter 1, 2, or 3.")

# make sure to select the co responding drawing to the difficulty selected 
def get_hangman_pics(difficulty):
     if difficulty==1:
          return drawings.HANGMAN_PICS_EASY
     elif difficulty==2:
          return drawings.HANGMAN_PICS_MEDIUM
     elif difficulty==3:
          return drawings.HANGMAN_PICS_HARD


#  a unility function that starts the game and initiate the functions above in variables , later will be more comfortable to call the variable the stores the function 
def play_hangman():
    # Setup game based on player choices
    difficulty = handle_difficulty()
    word = get_word()
    hangman_pics = get_hangman_pics(difficulty)
    guessed_word = ["_"] * len(word)
    # the set method is used to store the guessed letters in a single variable 
    guessed_letters = set()
    mistakes = 0
    

    print("\nLet's start Hangman!")
    print("The word has", len(word), "letters.")
    print(" ".join(guessed_word))

# game logic 
    while mistakes < len(hangman_pics) - 1:
        guess = input("\nGuess a letter: ").strip().lower()
         
        #  make sure the guess is not numeric using .isalpha()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        # cheking if the gussed letter was allready used 
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
    #   add each guessed letter into the variable that stores the letters with the set() method aboove 
        guessed_letters.add(guess)

#  cheking if the gueesed letter is inside the selected word
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("\nCorrect!")
        else:
            mistakes += 1
            print("\nWrong guess!")
        
        print(hangman_pics[mistakes])
        print(" ".join(guessed_word))

        if "_" not in guessed_word:
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

# Run the game 
if __name__ == "__main__":
    play_hangman()

