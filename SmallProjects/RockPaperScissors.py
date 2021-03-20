# Playing rock paper scissors with the computer
# Import random and initialize the counter. Create List with R,P,S
import random
counterPC = 0
counterUser = 0
listWithWords = ["Rock", "Paper", "Scissors"]

while True:
    rockPaperScissors = random.randint(0, 2)

    print("Enter Rock, Paper or Scissors")
    userInput = str(input())
    print("User input: " + userInput + " - " + "Computer: " + listWithWords[rockPaperScissors])

    if userInput == listWithWords[rockPaperScissors]:
        print("You entered the same, try again")

    elif userInput == "Rock" and listWithWords[rockPaperScissors] == "Paper":
        counterPC = counterPC + 1
        print("Your score: " + str(counterUser))
        print("Computer score: " + str(counterPC))
    elif userInput == "Rock" and listWithWords[rockPaperScissors] == "Scissors":
        counterUser = counterUser + 1
        print("Your score: " + str(counterUser))
        print("Computer score: " + str(counterPC))
    elif userInput == "Paper" and listWithWords[rockPaperScissors] == "Rock":
        counterUser = counterUser + 1
        print("Your score: " + str(counterUser))
        print("Computer score: " + str(counterPC))
    elif userInput == "Paper" and listWithWords[rockPaperScissors] == "Scissors":
        counterPC = counterPC + 1
        print("Your score: " + str(counterUser))
        print("Computer score: " + str(counterPC))
    elif userInput == "Scissors" and listWithWords[rockPaperScissors] == "Rock":
        counterPC = counterPC + 1
        print("Your score: " + str(counterUser))
        print("Computer score: " + str(counterPC))
    else:
        counterUser = counterUser + 1
        print("Your score: " + str(counterUser))
        print("Computer score: " + str(counterPC))

# Who won 3 rounds
    if counterUser == 3:
        print("You won!")
        break
    elif counterPC == 3:
        print("The computer won")
        break
