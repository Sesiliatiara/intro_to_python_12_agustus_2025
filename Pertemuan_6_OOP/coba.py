import random

# Card values
CARD_VALUES = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = list(CARD_VALUES.keys())

def create_deck():
    """Creates and shuffles a deck."""
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    """Calculates the hand's value, accounting for Aces."""
    value = sum(CARD_VALUES[card[0]] for card in hand)
    # Adjust for Aces
    num_aces = sum(1 for card in hand if card[0] == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        print('Dealer\'s hand: [Hidden],', hand[1])
    else:
        print('Hand:', ', '.join([f'{rank} of {suit}' for rank, suit in hand]))

def blackjack():
    print('Welcome to Blackjack!')

    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    display_hand(player_hand)
    display_hand(dealer_hand, hide_first_card=True)

    # Player's turn
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value > 21:
            print('You bust! Dealer wins.')
            return
        move = input('Hit or stand? (h/s): ').strip().lower()
        if move == 'h':
            player_hand.append(deck.pop())
            display_hand(player_hand)
        elif move == 's':
            break
        else:
            print('Invalid input. Type "h" to hit or "s" to stand.')

    # Dealer's turn
    print("\nDealer's turn:")
    display_hand(dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        print('Dealer hits.')
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if dealer_value > 21:
        print('Dealer busts! You win!')
        return

    # Compare hands
    print(f'\nYour value: {player_value}')
    print(f'Dealer value: {dealer_value}')
    if player_value > dealer_value:
        print('You win!')
    elif player_value < dealer_value:
        print('Dealer wins!')
    else:
        print('It\'s a tie!')

if __name__ == '__main__':
    blackjack()