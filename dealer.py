from random import randint
class Dealer:
    def __init__(self):
        self.card=0
        self.new_card=0

#This method gets a random number between 1 and 13, this method should be used when starting the game to get a number card. This represents the current card on the board
    def random_card(self):
        self.card=randint(1,13)
        # print(self.card)
        return self.card
    
#This method gets a random number between 1 and 13, this method represents the next card threw on the board, the number should be a higher or lower number than the random_card method
    def next_card(self):
        self.new_card=randint(1,13)
        while self.card == self.new_card:
            self.new_card=randint(1,13)

        print(self.new_card)
        return self.new_card

#deal=Dealer()
#deal.random_card()
#deal.next_card()


        
            





