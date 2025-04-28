import random

list_of_words = ["Abeokuta", "Abuja", "Lagos", "Ibadan", "PortHarcourt", "Enugu", "Kaduna", "Benin", "Calabar", "Owerri","Akure", "Jos", "Ilorin", "Yola", "Maiduguri", "Makurdi", "Asaba", "Uyo", "Aba", "Onitsha", "Warri", "Zaria", "Kano", "Sokoto", "Gombe", "Bauchi", "Kogi"]
word = random.choice(list_of_words).upper()
chance = int(len(word)/2)
print (f"""
Welcome to the game of Hangman!\nYou need to guess the name of a city (capital of a State) in Nigeria.\nThe name of the city to guess is represented by a row of dashes representing each letter.\n 
You can guess one letter at a time.\n  If you guess a letter that is in the word, it will be revealed in its correct position.\nIf you guess a letter that is not in the word, you lose a chance.\n  
    You have {chance} chances to guess the city correctly.\n\n""")

guess_word = "_ " * len(word)
print(f"The City has {len(word)} letters. Goodluck!!!\n{guess_word}\n")

list_of_letters = list(word)
#print(list_of_letters)
guessed_word_list = list(guess_word.split())

guess_list = []


while chance > 0:
    guess = input("Guess a letter: ")
    guess = guess.upper()

    #for letter in list_of_letters:
    if guess in list_of_letters:
        position = list_of_letters.index(guess)
        guess_list.append(guess)
        print(f"You guessed letter {position+1} correctly")
        guessed_word_list[position] = guess
        guessed_word = " ".join(guessed_word_list)
        print(guessed_word)
        
         
        list_of_letters[position] = "_"

        if "".join(guessed_word.strip().split()) == word:
            print(f"""
                  ******************************Congratulations, You won!****************************** \n
                  ***************You guessed the city of {word.upper()} correctly*************""")
            break
    elif guess.upper() in guess_list:
        print("You have already guessed that letter.")
    
    else:
        chance -= 1
        print(f"***************You guessed wrong. You have {chance} chances left***************")       
        if chance == 0:
            print(f"***************You lost!!!\nThe word was {word}***************")
            break



