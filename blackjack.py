import random

def create_deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_hand(deck):
    return [deck.pop() for _ in range(2)]

def calculate_score(cards):
    score = 0
    for card in cards:
        rank = card['rank']
        if rank == 'A':
            score += 11
        elif rank in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(rank)
    # score for Aces
    for card in cards:
        if card['rank'] == 'A' and score > 21:
            score -= 10
    return score

def display_cards(cards, player='Player'):
    print(f"{player}'s cards:")
    for card in cards:
        print(f"  {card['rank']} of {card['suit']}")
    print(f"Total Score: {calculate_score(cards)}")

def blackjack():
    player_cards = deal_hand(deck)
    dealer_cards = deal_hand(deck)

    display_cards(player_cards)
    print(f"Dealer's first card: {dealer_cards[0]['rank']} of {dealer_cards[0]['suit']}")

    
    if calculate_score(player_cards) == 21:
        display_cards(dealer_cards, player='Dealer')
        print("Blackjack! Player wins!")
        return

    while True:
        choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
        if choice == 'y':
            player_cards.append(deck.pop())
            display_cards(player_cards)
            if calculate_score(player_cards) > 21:
                display_cards(dealer_cards, player='Dealer')
                print("Bust! Player loses.")
                return
        elif choice == 'n':
            break

  
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deck.pop())

    display_cards(player_cards)
    display_cards(dealer_cards, player='Dealer')

   
    if calculate_score(dealer_cards) > 21:
        print("Dealer bust! Player wins!")
    elif calculate_score(player_cards) > calculate_score(dealer_cards):
        print("Player wins!")
    elif calculate_score(player_cards) < calculate_score(dealer_cards):
        print("Dealer wins!")
    else:
        print("It's a draw!")


deck = create_deck()
while True:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_again != 'y':
        break

    blackjack()