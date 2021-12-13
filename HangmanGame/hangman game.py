import sys
import random

a= True
while a==True :
    
 print("                  WELCOME TO HANGMAN GAME                       ")

 words_list = ['laptop', 'china', 'usa', 'canada',      
              'india', 'music', 'books', 'pen','mobile',                               # list of words to guess
              'enter', 'hello','apple','banana', 'mango',
              'strawberry', 'orange', 'grapes', 'pineapple', 'lemon' ]

                        
                        
 accepted_input = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']   # alphabet accepted by game
                                           
 word_guess = random.choice(words_list)     # choice randam word in from the word_list 
 word_to_guess = []
 for i in range(0, len(word_guess)):
     word_to_guess.append(word_guess[i])
 currently = []
 for i in word_to_guess:                    # fill in our currently guessed list with "_"
     currently.append("_")
 guess_letters = []
 guesses = 0



 if sys.version_info[0] < 3:
     input = raw_input

 def hangman_graphic(guesses):
     print("")
     print("Currently you know: ", end=" ")
     for i in range(0, len(currently)):
         print(currently[i], end=" ")
     print("")
     print("You have already tried letters:", end=" ") #for print a selected letter 
     for i in range(0, len(guess_letters)):
         print(guess_letters[i], end=" ")
     print("")
     if guesses == -1: #win graphic
         print("       0      ")
         print("     ~~|~~    ")
         print("      / \     ")
         print("______________")
         print("You just saved me!")
         print("YOU WIN!")
     elif guesses == 0:
         print("________      ")
         print("|      |      ")
         print("|             ")
         print("|             ")
         print("|             ")
         print("|             ")
         print("|_____________")
     elif guesses == 1:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|             ")
         print("|             ")
         print("|             ")
         print("|_____________")
     elif guesses == 2:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /       ")
         print("|             ")
         print("|             ")
         print("|_____________")
     elif guesses == 3:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /|      ")
         print("|             ")
         print("|             ")
         print("|_____________")
     elif guesses == 4:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /|\     ")
         print("|             ")
         print("|             ")
         print("|_____________")
     elif guesses == 5:
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /|\     ")
         print("|     /       ")
         print("|             ")
         print("|_____________")
     else:   # loose graphic
         print("________      ")
         print("|      |      ")
         print("|      0      ")
         print("|     /|\     ")
         print("|     / \     ")
         print("|             ")
         print("|_____________")
         print("The man was hang  ")
         print("The word was {}".format(word_guess))
         print("GAME OVER!")

 def guess_input():
     global guesses
     global currently
     global word_to_guess

     while True:
         user_input = input("Please input your guess (a single letter): ")   # if input is more than one letter print
         if user_input in accepted_input:
             if user_input in guess_letters:
                 print("You have already inputted this letter before, be more attentive!")
             else:
                 guess_letters.append(user_input)
                 if user_input in word_to_guess:
                                                                                 #for guess is right 
                     print("Well done, you guessed the right letter")
                     for i in range(0, len(word_to_guess)):
                         if word_to_guess[i] == user_input:
                             currently[i] = user_input
                 else:
                     print("Ops, there is no such letter in our word ")     #if guess letter is not present in word than print 
                     guesses = guesses + 1

         else:
             print("INPUT ERROR! Please input single letter in range a-z")  #if any input like(@#^&&@!234556) 

         if guesses > 5:                       #game over you lost
             hangman_graphic(guesses)
             break
         elif "_" in currently:                #keep playing
             hangman_graphic(guesses)
         else:                                  #game over you WON
             hangman_graphic(-1)
             break


 def hangman():
     hangman_graphic(guesses)             #this is a function to call graphic
     guess_input()


 if __name__ == "__main__":
    hangman()
    print("BYE BYE!")


 answer = input ("Do you want to play again ?")
 if answer == "yes":
   continue
 else:answer =="no"
 exit()
