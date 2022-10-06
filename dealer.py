from random import randint
class Dealer:
    def __init__(self):
        self.new_card=0
        self.current_card=0
        self.last_played=0

#This method gets a random number between 1 and 13, if there is not a last played card, the number is added to the list of last played cards.
    def random_new_card(self):
        self.new_card=randint(1,13)
        self.current_card=self.last_played
        if self.last_played==0:
            self.last_played=self.new_card
        print(self.new_card)
        return self.new_card
        
#This method stores the last played card to a list
    def get_last_played(self):
        self.last_played=self.current_card
        print(self.last_played)
        return self.last_played
        

#deal=Dealer()
#deal.random_new_card()
#deal.random_new_card()
#deal.get_last_played()
#deal.random_new_card()
#deal.get_last_played()


