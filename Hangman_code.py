# Importing modules & other .py files for it working.
import random
import Hangman_words 
from Hangman_art import logo, win, lose, stages
print(logo)
# Variable declared for Loop
gameOn = True
# Loop to keep the gamming running as per user choice 
while(gameOn==True):
# MAIN GAME CODE
     newGame = int(input("\nPress 1 to Start, Press any number key to Exit\n"))
     if(newGame == 1):
          lives = 6
          end_of_game = False
          chosen_word = random.choice(Hangman_words.word_list)
          word_length = len(chosen_word)
#For debug purposes
          #print(f'Solution is {chosen_word}.')

          # Adding dashes in code & replacing them with the correct guess
          display = []
          for _ in range(word_length):
               display += "_"

          while not end_of_game:
               guess = input("Guess a Letter :: ").lower()
# Prompting user that he already guessed the word and no effect will take place
               if guess in display:
                    print(f"You've already guessed {guess}")

               for position in range(word_length):
                    letter = chosen_word[position]

                    if letter == guess:
                         display[position] = letter
# Prompting user with message that a wrong letter is entered and loose a life 
               if guess not in chosen_word:
                    print(f"You guessed {guess}, thats not in the word. You lose a life")  
                    lives-=1
                    print(stages[lives])  
                    if lives == 0:
                         # Ending the game when lives = 0
                         end_of_game = True
                         print(f"{lose}\n")
                         # Showing user/player what the correct word was.
                         print(f"\nThe Chosen word was '{chosen_word}")

               print(f"{' '.join(display)}")
               
               # Ending the game with win
               if'_'not in display:
                    end_of_game=True
                    print(f"{win}\n")

# User choice to exit the game
     else: 
          print("Thank You...! Exiting...")
          gameOn = False
