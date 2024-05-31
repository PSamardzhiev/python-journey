import random
import hangman_pics as hpp

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
    choise = input("Enter your guess: ")
    if choise in ran_word:
        for index in range(len(ran_word)):
            if choise == ran_word[index]:
                display[index] = choise
        print(display)
    else:
        print(display)
        player_attempts -= 1
        print(f"Wrong answer, you have {player_attempts} attempts left to try ")
        print(hpp.HANGMANPICS[int(hang_draw)])
        hang_draw += 1

if player_attempts > 0:
    
    print("You win!")
else:
    
    print("You lost")
