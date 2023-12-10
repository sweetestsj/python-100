############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def clear():  # Cross-platform clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card(deck: list[int]):
    deck.append(random.choice(cards))

def calculate_score(deck: list[int]):
    possible_scores=[]
    deck_sum = sum(deck)
    possible_scores.append(deck_sum)
    num_aces = deck.count(11)
    for _ in range(num_aces):
        deck_sum -= 10
        possible_scores.append(deck_sum)
    if len(possible_scores) == 1:
        return possible_scores[0]
    else:
        for score in possible_scores:
            if score <= 21:
                return score
        return possible_scores[-1]

def printResult(message: str, user_deck: list[int], dealer_deck: list[int]):
    print(f"{message}, your score: {calculate_score(user_deck)}, dealer score: {calculate_score(dealer_deck)}, your cards: {user_deck}, dealer cards: {dealer_deck}")

def compare_score(user_deck: list[int], dealer_deck: list[int]):
    # return 1 if user wins, 0 if draw, -1 if dealer wins
    user_score = calculate_score(user_deck)
    dealer_score = calculate_score(dealer_deck)
    if dealer_score > 21:
        return True, 1, "dealer bust!"
    elif dealer_score == 21:
        return True, -1, "dealer black jack!"
    elif user_score > 21:
        return True, -1, "You bust!"
    elif user_score == 21:
        return True, 1, "you black jack!"
    elif user_score - dealer_score > 0:
        return False, 1, "you won!"
    elif user_score - dealer_score < 0:
        return False, -1, "dealer won!"
    else:
        return False, 0, "draw!"


dealer_wins = 0
user_wins = 0

dealer_deck=[]
user_deck=[]

while True:
    clear()
    print(logo)
    dealer_deck = []
    user_deck = []
    print(f"You: {user_wins} win {dealer_wins} loss")
    print(f"Dealer: {dealer_wins} win {user_wins} loss")
    should_start_game = int(input("do you want another game? type 0 if yes, 1 if no\n"))
    if should_start_game != 0:
        break
    while calculate_score(dealer_deck) < 17:
        deal_card(dealer_deck)
    deal_card(user_deck)
    deal_card(user_deck)
    while True:
        is_game_ending, score, message = compare_score(user_deck, dealer_deck)
        if is_game_ending:
            if score == 1:
                user_wins += 1
            else:
                dealer_wins +=1
            printResult(message, user_deck, dealer_deck)
            input("Type enter to continue...\n")
            break
        print(f"Your cards: {user_deck}")
        should_draw_card = int(input("do you want draw another card? type 0 if yes, 1 if no\n"))
        if should_draw_card == 0:
            deal_card(user_deck)
        else:
            if score == 1:
                user_wins += 1
            elif score == -1:
                dealer_wins +=1
            printResult(message, user_deck, dealer_deck)
            input("Type enter to continue...\n")
            break

    
#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
#Bug fix. If you and the computer are both over, you lose.

#Hint 5: Deal the user and computer 2 cards each using deal_card()
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
