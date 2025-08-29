from abc import ABC, abstractclassmethod
import random
class Kartu(ABC): 
    __SUIT = ["♣️", "♥️", "♠️", "♦️"] 
    __RANK = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    _total_kartu : 52
    __total_deck = 1
    __deck=[]

    @abstractclassmethod
    def getWin(): #
        pass

    def __init__(self, total_deck = 1): 
        self._total_kartu = total_deck
        for i in range(self.__total_deck):
            self.make_deck()

    def make_deck(self): 
        for s in self.__SUIT:
            for r in self.__RANK:
                card = (s,r)
                self.__deck.append(card)
        self._total_kartu = len(self.__deck)
        random.shuffle(self.__deck)

    def information_deck(self):
        print(f"Jumlah deck : {self.__total_deck}")
        print(f"Jumlah kartu : {self._total_kartu}")

    def getCard(self): 
        text = ""
        card = []
        card.append(self.__deck.pop())
        for s,r in card:
            text += "[" + r + s + "]"
        return text
    
    def setDeck(self,total_deck):
        self.__deck = []
        self.__total_deck = total_deck
        for i in range(self.__total_deck):
                self.make_deck()

class BlackJack(Kartu):
    def information():
        print("========BlackJack========")
    

    def getWin():
        print("Player Win!")

# card = Kartu()
# card.information_deck()
game = BlackJack()
game.information_deck()