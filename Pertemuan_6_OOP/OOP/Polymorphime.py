import random
class Kartu(): 
    __SUIT = ["♣️", "♥️", "♠️", "♦️"] 
    __RANK = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    _total_kartu : 52
    __total_deck = 1
    __deck=[]
    
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

    def information(self):
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
    def information(self):
        print("========BlackJack========")
        super().information() #coba tanya dipertemuan berikutnya harus pakai ini atau tidak soalnya kalo gak ini tidak tercetak
    
class Poker(Kartu):
    def information(self):
        print("========Poker========")
        super().information()

card = Kartu()
game1 = BlackJack()
game2 = Poker()

def information(Kartu):
    Kartu.information()

information(card)
information(game1)
information(game2)

