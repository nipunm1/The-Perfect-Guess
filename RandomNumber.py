import random

class RandomNumber:

    @staticmethod
    def play(playerChoice):
        number_of_guess = 0
        ran_no = random.randint(1,10)
        while(True):
            if(playerChoice>ran_no):
                print("Press 0 to quit")
                print("Lower Number Please")
                number_of_guess = number_of_guess+1
            elif(playerChoice<ran_no):
                print("Press 0 to quit")
                print("Higher Number Please")
                number_of_guess = number_of_guess+1
            elif(playerChoice == ran_no):
                print("Perfect Guess")
                print("Total guess = ",number_of_guess)
                break    
            playerChoice = int(input("Guess Again between 1 to 10: "))
            if(playerChoice==0):
                print("Guess number = ",ran_no," better luck next time :)")
                break
        with open("hiscore.txt","r") as f:
            hiscore = f.read()
        if(hiscore == ""):
            with open("hiscore.txt","w") as f:
                f.write(str(number_of_guess))
        else:
            if(int(hiscore) < number_of_guess):
                print("You just beat the high score")
                with open("hiscore.txt","w") as f:
                    f.write(str(number_of_guess))

r = RandomNumber()
choice = int(input("Guess The Number between 1 to 10: "))
r.play(choice)            
