import random
import hangman_art as hma

word_list = ["apple","orange","pear","strawberry","pineapple"]
player_attempts = 7
hang_draw = 0
ran_word = random.choice(word_list)

# if you want to cheat just uncomment below:
# print(f"Pssst, a little cheat, your word is {ran_word}")
display = []

for _ in range(len(ran_word)):
    display.append("_")

print(display)

while "_" in display and player_attempts > 0:
    choice = input("Enter your guess: ")
    if choice in ran_word:
        for index in range(len(ran_word)):
            if choice == ran_word[index]:
                display[index] = choice
        print(display)
    else:
        print(display)
        player_attempts -= 1
        print(f"Wrong answer, you have {player_attempts} attempts left to try ")
        print(hma.HANGMANPICS[int(hang_draw)])
        hang_draw += 1

if player_attempts > 0:
    
    print("You win!")
else:
    
    print("You lost")
