# PA06: Blackjack
# Carson Crenshaw
# cgc8gdt

# Function #1
def card_to_value(card):
    """
     This function produces the numeric value of a single card delt in blackjack.
    :param card: This function takes as input a str variable representing a single card in blackjack.
    :return: This function returns the numeric blackjack score of the card.
    """
    if card == "2" or card == "3" or card == "4" or card == "5" or card == "6" or card == "7" or card == "8" or card == "9":
        cardval = int(card)
    elif card == "T" or card == "J" or card == "Q" or card == "K":
        cardval = 10
    else:
        cardval = 1
    return cardval

# Function #2
def hard_score(hand):
    """
    This function returns the “hard” score of the hand, where all aces are treated as one.
    :param hand: This function takes as input a str variable where each character in the str is a card.
    :return: This function returns the sum of the points value of each card.
    """
    total = 0
    for i in hand:
        # Call card_to_value function within new function
        hardscore1 = card_to_value(i)
        total = total + hardscore1
    return total

# Function #3
def soft_score(hand):
    """
    This function returns the "soft" score of the hand, where all aces are treated as one EXCEPT the first ace which is treated as 11.
    :param hand: This function takes as input a str variable where each character in the str is a card.
    :return: This function returns the sum of the points value of each card.
    """
    if "A" in hand:
        total2 = 10
        for i in hand:
            # Call card_to_value function within new function
            softscore1 = card_to_value(i)
            total2 = total2 + softscore1
        return total2
    else:
        total2 = 0
        for i in hand:
            softscore1 = card_to_value(i)
            total2 = total2 + softscore1
        return total2

