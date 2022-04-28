import random


def play(word):
    mychoice = input("Choose a category: 1. Star Wars 2. Animals 3. Superheroes. Type 1, 2, or 3: \n")
    if mychoice == "1":
        word = random.choice(starwars)
    if mychoice == "2":
        word = random.choice(animals)
    if mychoice == "3":
        word = random.choice(superheroes)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                print ("Guessed Letters: " ([guessed_letters]))
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                print ("Guessed Letters: "[guessed_letters])
                print(guessed_letters, " have been guessed")
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

starwars = ["anakinskywalker","jabathehutt","obiwankenobi","kashyyk","calkestis","maytheforcebewithyou","darthvader","countdoku","ashoka","padmeamidala","tatooine","naboo","darthmalgus","darthrevan","lightsaber","forceweilders","oldrepublic","jedicouncil","revengeofthesith","padawan"]
animals = ["zebra","dog", "horse", "panda", "cat", "mouse", "elephant", "tiger", "lion", "cheetah", "giraffe", "octopus", "racoon", "fox", "wolf", "monkey", "gorilla", "chimpanzee", ]
superheroes = ["captainamerica", "ironman", "hulk", "batman", "flash", "superman", "wonderwoman", "blackwidow", "aquaman", "catwoman", "greenlantern", "spiderman", "deadpool", "daredevil"]
word = ""
print("Welcome to Hangman!")
play(word)
 
def main():
    while input("Play Again? (Y/N) ").upper() == "Y":
        play(word)
    print("Thank you for playing!")


if __name__ == "__main__":
        main()
