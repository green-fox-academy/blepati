# Create a Card class, that has a color and a value
# Create a constructor for setting those values
# Card should be represented as string in this format:
# 9 Hearts
# Jack Diamonds
# Create a Deck class, that has a list of cards in it
# Create a constructor that takes a whole number as parameter
# The constructor should fill the list with the number of different cards using at least 4 different colors (except if the number given is smaller than four, than all cards should have different colors)
# We should be able to shuffle the deck, which randomly orders the cards
# We should be able to draw the top card which returns the drawn card and also removes it from the deck
# Deck should be represented as string in this format:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
import random

class Card(object):
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        card = create_one_card()
        return card[0] +" " + card[1]

class Deck(object):
    def __init__(self, num_of_cards):
        self.list_of_cards = []
        self.colors_of_cards = ["Club", "Diamond", "Heart", "Spade"]
        self.values_of_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.num_of_cards = num_of_cards

    def create_one_card(self):
        card = random.sample(self.colors_of_cards, 1) + random.sample(self.values_of_cards, 1)
        return card

    def create_deck(self):
        while len(list_of_cards) != self.num_of_cards:
            if
            self.list_of_cards.append(self.create_one_card())

    def shuffle_deck(self):
        shuffled_deck = random.shuffle(self.list_of_cards)
        return shuffled_deck

#cards = Card()
deck = Deck(12)
deck.create_deck()
deck.list_of_cards
deck.shuffle_deck()
deck.list_of_cards
# Should print out:
# 12 cards -  3 Clubs, 3 Diamonds, 3 Hearts, 3 Spades
#top_card = deck.draw()
#print(top_card)
#print(deck)
# Should print out:
# Queen Spades
# 11 cards - 3 Clubs, 3 Diamonds, 3 Hearts, 2 Spades
