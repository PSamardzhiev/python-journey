from art import game_logo
import random

number = random.randint(1,100)
player_lives = int()

print(game_logo)
print("Welcome to Python Number guessing game")
level = input("Please select the game difficulty by typing 'easy' or 'hard': ").lower()

if level == "easy":
    player_lives = 10
else:
    player_lives = 5

def game():
    global player_lives
    print(f"I am guessing a number between 1 and 100, take your chance, you have {player_lives} attempts: ")
    while player_lives > 0:
        guessed_number = int(input("Type your number: "))
        if guessed_number > number:
            player_lives -= 1
            print(f"Your number {guessed_number} is too high, you have {player_lives} remaining attempts!")
        elif guessed_number < number:
            player_lives -= 1
            print(f"Your number {guessed_number} is too low, you have {player_lives} remaining attempts!")
        else:
            print(f"Thats right, you guessed it, the correct number is {guessed_number}")
    else:
        print(f"Game over man!, the correct answer is {number}")

game()
