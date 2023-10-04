# Name: Brandon Mantuano
# Email: brandon.mantuano45@myhunter.cuny.edu
# Program #48: Guess the number a user is thinking of in their mind

import random 

def validFeedback():
    print("1: too small  2: too big  3: just right")
    feedback = int(input("Enter choice 1-3: "))

    while feedback != 1 and feedback != 2 and feedback != 3:
        feedback = int(input("Enter choice 1-3: "))

    return feedback

def guessGame():
    #TODO: set start to be 0 and end to be 100
    start = 0
    end = 100

    print("Pick an integer in [" + str(start) + ", " + str(end) + "] in your mind.")

    numGuesses = 1
    guess = (start+end//2)
    
    #TODO: set variable numGuesses to be 1 
    
    print("Guess " + str(numGuesses) + ": is it " + str(guess) + "?")

    feedback = validFeedback()

    #user does not choose "3. just right" yet
    while feedback != 3: 
        if feedback == 1: #too small
           start = guess + 1
        else:
            end = guess - 1
             
        guess =(start+end)//2

        numGuesses = numGuesses + 1

       

        if start == end:
           print("Guess " + str(numGuesses) + ": the answer must be", guess)
           return
           #TODO: leave the current function 
           #by calling return statement, 
           #since we find the answer
           #and finish guess game now. 

        print("Guess " + str(numGuesses) + ": is it " + str(guess) + "?")
        feedback = validFeedback()
        
    print("congratulations! The answer is " + str(guess))

   
def main():
    guessGame()
    
if __name__ == "__main__":
    main()

