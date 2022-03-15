import random

attempts = []

def add_attempt(number):
  attempts.append(number)

def start_game():
    print("Welcome to \"Can You Guess the Number?\"")
    player_name = input("Please enter your name: ")
    print("Instructions: {} guess a number between 1 and 100!".format(player_name))

answer = random.randint(1, 100)
tries = 0

start_game()
while True:
    try:
    guess = int(input("Enter your guess: "))
        if guess > 100:
            raise ValueError("Guess has to be a number between 1 and 100")
        elif guess < 1:
            raise ValueError("Guess has to be a number between 1 and 100")
            
    except ValueError as err:
        print("That is not a valid value, try again.")
    
    else:
        if guess == answer:
          print("You got it!")
          break
        elif guess > answer:
          print("It's lower.")
          continue
        elif guess < answer:
          print("It's higher.")
          continue
            
print("It took you {} attempts.".format(tries))

new_game = input("Would you like to play again? (Y/N)  ")
refresh = new_game.upper()
if refresh == "Y":
  start_game()
elif refresh == "N":
  print("Thank you for playing!")