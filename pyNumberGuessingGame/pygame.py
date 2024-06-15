from random import randint
from art import logo

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

answer = randint(1,100)

def set_difficulty():
  level = input("Choose difficulty by typing 'easy' or 'hard':  ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high. ")
    return turns - 1
  elif guess < answer:
    print("Too low. ")
    return turns - 1
  else:
    print(f"  You got it, the correct answer was {answer}")

def game():
  guess = 0
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  turns = set_difficulty()
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns = check_answer(guess, answer, turns)
  if turns == 0:
    print("You ran out of guesses. ")
    return 
  elif guess != answer:
    print("Give it another go")

game()

    
  