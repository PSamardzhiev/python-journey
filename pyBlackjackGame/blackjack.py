import random, os
from art import logo

def deal_card():
    """ Returns a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Takes a list of cards and return the score calculated from the cards'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return f"Draw with {user_score}, {computer_score}"
        elif computer_score == 0:
            return "Lose, opponent has Blackjack :( "
        elif user_score == 0:
            return "WIN with a Blackjack :) "
        elif user_score > 21:
            return f"You went over with score {user_score} and you lose "
        elif computer_score > 21:
            return f"Computer went over with score {computer_score} and you win!"
        elif user_score > computer_score:
            return f"You win with score {user_score}"
        else:
            return f"Computer wins with score {computer_score}"
        
        

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards {user_cards} and your score {user_score}")
        print(f"    Computer first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer final hand: {computer_cards}, final score: {computer_score}")

    print(compare(user_score, computer_score))


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you wanna play a game of Blackjack? Type 'y' or 'n':    ") == "y":
    os.system('cls')
    os.system('clear')
    play_game()