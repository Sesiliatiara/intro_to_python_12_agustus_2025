# case
# Kartu
import random

class Kartu: #Kartu ini nama dari class
    __SUIT = ["♣️", "♥️", "♠️", "♦️"] # _ _ ini disebut property atau sifat ini memiliki sifat protected
    __RANK = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    _total_kartu : 52
    __deck = []

    def __init__(self, total_kartu = 52): #ini disebutnya constructor
        self._total_kartu = total_kartu
        self.make_deck()

    def make_deck(self): #metode
        for s in self.__SUIT:
            for r in self.__RANK:
                card = (s,r)
                self.__deck.append(card)
        random.shuffle(self.__deck)

    def getDeck(self):
        return self.__deck

    def getCard(self): 
        text=""
        card = []
        card.append(self.__deck.pop())
        for s,r in card:
            text += "[" + r + s + "]"
        return text

deck = Kartu() #ini cara memanggil class
card = deck.getCard() #ini cara memanggil method
deck.total_kartu = 56
total_kartu = deck.total_kartu
print(card)
print(f"Total kartu : {total_kartu}")
