import random

print("Welcome to Hangman! The category is Star Wars.")

answers = ["Anakin Skywalker","Jaba the Hutt","Obi Wan Kenobi","Kashyyk","Cal Kestis","May the Force Be With You","Darth Vader","Count Doku","Ashoka","Padme Amidala","Tatooine","Naboo","Darth Malgus","Darth Revan","Lightsaber","Force Weilders","Old Republic","Jedi Council","Revenge of the Sith","Padawan"]

def get_word():
    word = random.choice(answers)
    return word.upper()

def play(word):
   word_completion = "_" * len(word)
   guessed = False
   guessedletters = []
   guessedwords = []
   tries = 6
   print(hangman_drawing(tries))
   print(word_completion)
   print("\n")
   while not guessed and tries > 0:
       guess = input("Please guess a letter or word.").upper()
       if len(guess) == 1 and guess.isaplpha():
          if guess in guessedletters:
            print ("You already guessed the letter", guess)
          elif guess not in word:
             print(guess, "is not in the word.")
             tries -=1
             guessedletters.append(guess)
          else:
            print(guess, "is in the word.")
            guessedletters.append(guess)
            word_as_list = list(word_completion)
            indices = [i for i, letter in enumerate(word) if letter == guess]
            for index in indices:
                word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
       elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedwords:
                 print("You already guessed the word" , guess)
            elif guess != word:
                print(guess, "is not in the word")
                tries -= 1
                guessedwords.append(guess)
            else:
                guessed = True
                word_completion = word
       else:
        print("Not a valid guess.")
        print(hangman_drawing(tries))
        print(word_completion)
        print("\n")
        if guessed:
            print("Cool, you won.")
        else:
            print("Sorry, you lost. The word was," + word)


def hangman_drawing(tries):
    levels = [  """ 
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                   ---
                """,
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                   ---
                """,
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
                   ---
                """,
                """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                   ---
                """,
                """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                   ---
                """,
                """
                    --------
                    |      |
                    |      O
                    |      
                    |      
                    |     
                   ---
                """,
                """
                    --------
                    |      |
                    |      
                    |      
                    |      
                    |     
                   ---
                """
    ]
    return levels[tries]
    
def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
