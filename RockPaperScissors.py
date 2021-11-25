import random

def RockPaperScissors():
    for x in range(5):
        print("")
    val = input("Pick Rock, Paper or Scissors (Case Sensitive): ")
    if (val == "Rock") or (val == "Paper") or (val == "Scissors") :
        print("")
        player1 = ["Rock", "Paper", "Scissors"]
        x = random.choice(player1)
        print("The computer chose: " + x)
        print("")

        if ((val == "Rock") and (x == "Rock") or (val == "Paper") and (x == "Paper") or (val == "Scissors") and (x == "Scissors")):
            print("Draw!")
        elif ((val == "Rock") and (x == "Scissors") or (val == "Scissors") and (x == "Paper") or (val == "Paper") and (x == "Rock")):
            print("You Win!")
        elif (val == "Rock") and (x == "Paper") or (val == "Paper") and (x == "Scissors") or (val == "Scissors") and (x == "Rock"):
            print("You Lose!")
    else:
        print("Please put in another value")
        RockPaperScissors()
RockPaperScissors()
