from card import Card
from itertools import product

class Player():
    """
    class that defines a player by the following attributes: 
    cards the player has at hand, the number of player's turn, 
    the amount of cards the player has, 
    the history of cards used by the player
    """  
    def __init__(self,cards,turn_count,number_of_cards,history):
        self.cards = Card
        self.turn_count = turn_count
        self.number_of_cards = ()
        self.history=[]

    def play(self):
        """
        Pick a card, add it to the history of a player, print something, return the card
        """
        from random import randint
        self.cards
        print (f"{Player} {turn_count} played: {value} {icon}")
        return Card


class Deck():
    def __init__(self,cards):
        self.cards = []
        
    def fill_deck(self):
        """
        create a full deck with all the cards
        """
        Symbols = ["♥", "♦", "♣", "♠"]
        Values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = list(itertools.product(Symbols, Values))
        return self.cards

    def shuffle(self):
        """
        shuffle all the list of cards
        """
        from random import shuffle
        random.shuffle(cards)
        
    def distribute(self):
        """
        take Player as a parameter and distribute cards evenly between all players
        """
        from random import sample
        for Player in :
            random.sample(cards, num)
        





