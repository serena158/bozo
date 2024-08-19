import random
from colorama import Fore, Back, init
init(autoreset=True)
from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses
from colorama import init, Fore, Back, Style

def valid_guess(guess: str) -> bool:
     if guess.upper() in get_valid_wordle_guesses():
          return True
     else:
          return False
    
def get_feedback(guess: str, secret_word: str) -> str:
    returned_value = ['-','-','-','-','-']
    guess = guess.lower()
    guess1 = guess.upper()
    secret_word = secret_word.lower()
   
    guess = [*guess]
    secret_word = [*secret_word]
     
    temp_secret_word = [*secret_word]

    for i in range(0,len(guess)):
            if guess[i] == secret_word[i]:
                returned_value[i] = guess[i].upper()
                temp_secret_word[i] = '*'
                
    for i in range(0,len(guess)):
         for m in range(len(temp_secret_word)):
              if guess[i] == temp_secret_word[m] and not returned_value[i].isalpha():
                   returned_value[i] = guess[i]
                   temp_secret_word[m] = '*'
    
    feedback = ''.join(returned_value)
    colorsvar = ""
    counter = 0
    init()

    for i in feedback: 
         if i == '-':
              colorsvar = colorsvar + Fore.WHITE + Back.LIGHTBLACK_EX + guess1[counter] + Style.RESET_ALL
         elif ord(i) > 90:
              colorsvar = colorsvar + Fore.WHITE + Back.YELLOW + guess1[counter] + Style.RESET_ALL
         else:
              colorsvar = colorsvar + Fore.WHITE + Back.GREEN + guess1[counter] +Style.RESET_ALL
         counter+=1
    print(colorsvar)
    return feedback

correct_indices = ['!','!','!','!','!']
potentialguess = list(get_secret_words())

import time
import sys

if __name__ == "__main__":
    secret_word = 'BRAVE'
    #random.choice(list(get_secret_words()))
    guess='crane' #change to ''
    'secret_word.lower() != guess.lower():'
    guess_count = 0
    while guess_count <= 4:
        
        guess = input('Enter guess: ') 

        
        while valid_guess(guess) == False:
             print("Input invalid, ensure no special characters, incorrect lengths or numbers and try again: ")
             guess = input('Enter guess: ')
        
        get_feedback(guess, secret_word)
        guess_count += 1
    

        if secret_word.lower() == guess.lower():
            animation = "◕‿◕ ◠‿◠"
            print("     You win!!!",end="")
            start_time = time.time()
            while True:
                for i in range(0,9,4):
                    time.sleep(0.2) 
                    sys.stdout.write("\r" + animation[i:i+4 % len(animation)])
                    sys.stdout.flush()
                if time.time() - start_time > 10:  # The animation will last for 10 seconds
                    break
            break
        
    if guess_count == 5 and secret_word.lower() != guess.lower():
        print('All out bozo! The word was ', secret_word, ':(') 

 
    pass