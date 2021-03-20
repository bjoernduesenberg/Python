# This is a number guessing game
# Import random module to create random numbers
import random

# Create number between 1 and 50
randomNumber = random.randint(1, 50)

# The user should enter a number
print("Please enter a number between 1 and 50: ")
userInput = int(input())
print(userInput)

# Check if the users number is between 1 and 50 until correct
while userInput < 1 or userInput > 50:
    if userInput < 1:
        print("Please enter a number between 1 and 50")
        userInput = int(input())
    elif userInput > 50:
        print("Please enter a number between 1 and 50")
        userInput = int(input())

# Check if the number is correct until correct
while userInput != randomNumber:
    if userInput < randomNumber:
        print("Your number is too low")
        print("Enter your next number: ")
        userInput = int(input())
    elif userInput > randomNumber:
        print("Your number is too high")
        print("Enter your next number: ")
        userInput = int(input())

print("Your answer was correct!")
