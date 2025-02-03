import random
def guess_numb ():
    print ("Hello! What is your name?")
    name = input()
    random_numb = random.randint(1,20)
    print ("Well, "+ name + ", I am thinking of a number between 1 and 20.")
    guess = 0
    while True :
        print ("Take a guess")
        my_guess = int(input())
        guess +=1
        if my_guess < random_numb:
            print("Your guess is too low.")
    
        elif  my_guess > random_numb:
        
          
           print("Your guess is too high.")
        
        else:
         print("Good job," + name + "! You guessed my number in " + str(guess) + " guesses!")
         break
guess_numb ()