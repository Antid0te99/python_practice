
from black_jack_art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
dealer_cards = []

def deal_card():
    return random.choice(cards)

def calculate_score(card_list):

    total = sum(card_list)
    if total > 21 and 11 in card_list:
        card_list[card_list.index(11)] = 1
        total = sum(card_list)
    return total

def compare(user_total, dealer_total):
    if user_total == dealer_total:
        return "Draw"
    elif dealer_total == 21:
        return "Lose, opponent has Blackjack"
    elif user_total == 21:
        return "Win with a Blackjack"
    elif user_total > 21:
        return "You went over. You lose"
    elif dealer_total > 21:
        return "Opponent went over. You win"
    elif user_total > dealer_total:
        return "You win"
    else:
        return "You lose"

def play_blackjack():
    print(logo)

    user_cards.clear()
    dealer_cards.clear()

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_total = calculate_score(user_cards)
        dealer_total = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_total}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_total == 21 or dealer_total == 21 or user_total > 21:
            game_over = True
        else:
            user_choice = input("Type 'y' to add another card and 'n' to pass: ")
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while dealer_total < 17 and dealer_total != 21:
        dealer_cards.append(deal_card())
        dealer_total = calculate_score(dealer_cards)

    print(f"Your final cards: {user_cards}, final score: {user_total}")
    print(f"Dealer's final cards: {dealer_cards}, final score: {dealer_total}")
    print(compare(user_total, dealer_total))

while input("Do you want to play Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_blackjack()
