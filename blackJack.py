from os import system, name
from random import randint
from random import shuffle


standard_deck_of_cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
deck_of_cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

def blackjack():
    deck_of_cards=standard_deck_of_cards
    shuffle(deck_of_cards)

    player_hand = []
    dealer_hand = []
    for _ in range(2):
        player_hand.append(deck_of_cards.pop())
        dealer_hand.append(deck_of_cards.pop())

    running = True
    while running:
        
        end_turn = False
        
        player_score = sum(player_hand)
        dealer_score = sum(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer cards: {dealer_hand}, current score: {dealer_score}")

        if dealer_score <= 16:
            dealer_hand.append(deck_of_cards.pop())
        else:
            pass

        hit = input("press 'h' to hit: ")
        if hit == "h":
            player_hand.append(deck_of_cards.pop())
        else:
            end_turn = True

        dealer_score = sum(dealer_hand)
        player_score = sum(player_hand)
        
        if player_score > 21:
            for ace in player_hand:
                if ace == 11:
                    player_hand.remove(11)
                    player_hand.append(1)
                    player_score = sum(player_hand)
            if player_score > 21:
                running = False


        if dealer_score > 21:
            for ace in dealer_hand:
                if ace == 11:
                    dealer_hand.remove(11)
                    dealer_hand.append(1)
                    dealer_score = sum(dealer_hand)
            if dealer_score > 21:
                running = False

        if end_turn == True and dealer_score > 16:
            running = False
        elif end_turn == True and dealer_score < 16:
            while dealer_score <= 16:
                dealer_score = sum(dealer_hand)
                if dealer_score > 21:
                    running = False
                dealer_hand.append(deck_of_cards.pop())
        else:
            pass
            
        
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Dealer cards: {dealer_hand}, current score: {dealer_score}")
    if player_score > 21:
        print("\nbust")
    elif dealer_score < player_score <= 21:
        print("\nyou win")
    elif player_score <= 21 and dealer_score > 21:
        print("\nyou win")
    elif player_score < dealer_score <= 21:
        print("\nyou lose")
    elif player_score == dealer_score:
        print("\ndraw")

    


def main():
    blackjack()
    
running = True
while running:
    main()

