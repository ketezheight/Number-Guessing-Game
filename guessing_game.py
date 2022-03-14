import random

def start_game():
    print("Welcome to \"Can You Guess the Number?\"")
    player_name = input("Please enter your name: ")
    print("Instructions: {} guess a number between 1 and 100!".format(player_name))

answer = random.randint(1, 100)

start_game()
