import random
import Hangman_words
from Hangman_art import logo, win, lose, stages
print(logo)
a=1
while(a==1):
     newGame = int(input("\nPress 1 to Start, Press any number key to Exit\n"))
     if(newGame == 1):
          lives = 6
          end_of_game = False
          chosen_word = random.choice(Hangman_words.word_list)
          word_length = len(chosen_word)
#For debug purposes
          #print(f'Solution is {chosen_word}.')

          display = []
          for _ in range(word_length):
               display += "_"

          while not end_of_game:
               guess = input("Guess a Letter :: ").lower()

               if guess in display:
                    print(f"You've already guessed {guess}")

               for position in range(word_length):
                    letter = chosen_word[position]

                    if letter == guess:
                         display[position] = letter
#     print(f"{' '.join(display)}")
               if guess not in chosen_word:
                    print(f"You guessed {guess}, thats not in the word. You lose a life")  
                    lives-=1
                    print(stages[lives])  
                    if lives == 0:
                         end_of_game = True
                         print(f"{lose}\n")
                         print(f"\nThe Chosen word was '{chosen_word}")

               print(f"{' '.join(display)}")

               if'_'not in display:
                    end_of_game=True
                    print(f"{win}\n")

               # print(stages[lives])  
     else: 
          print("Thank You...! Exiting...")
          break
