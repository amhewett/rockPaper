'''
Created on Feb 1, 2020

@author: ITAUser
'''
#set variable keepPlaying to true
#While keepPlaying is true:
    
    #print statement welcoming players to the game
    #print statement stating the rules (best 2 out of 3 Press 'q' to quit)
    
    #make a key that assigns a number to each choice for the computer
    #rock is 1, scissors is 2, paper is 3)
    
    #import the random function - the computer makes its choice randomly from this function

    #set computer's score to 0
    #set player's score to 0
    
    #while player's score is less than 2 and the computer's score is less than 2: -- this means the game is still on
    
        #computer's choice = random number between 1 and 3(Random function gets used here)
        #player's choice = input(ask player to select Rock, Paper, or Scissors)
        
        #start checking user options
        #userChoice = userChoice.lower()
        #if player inputs 'q': --we want to end the game
            #set keepPlaying to False --ends the loop
            #stop the loop -- yay! break statement
         
        #else if (player inputs rock and computer chooses rock) or
        #(player inputs paper and computer chooses paper) or
        #(player inputs scissors and computer chooses scissors):
            #print out DRAW
            #print out player's score and computer's score
            
        #else if (player inputs rock and computer chooses scissors) or
        #(player inputs scissors and computer chooses paper) or
        #player inputs paper and computer chooses rock):
            #add one to the player's score
            #print out player's score and computer's score
            #print out "YAY"
            
        #else if (player inputs scissors and computer chooses rock) or
        #(player inputs paper and computer chooses scissors) or
        #player inputs rock and computer chooses paper): 
            #add one to the computer's score
            #print out player's score and computer's score
            #print out "Dangit!"
        
        #else:
            #tell the user their input was not valid
            
    #print statement thanking the players for playing
    #if player's score is 2:
        #print statement letting player know they won
     #if computer's score is 2:
        #print statement letting player know the computer won
     #print out player's score and computer's sco