from random import randint
class Dealer:
    def __init__(self):
        self.new_card=0

    def random_new_card(self):
        self.new_card=randint(1,13)
        print(self.new_card)

deal=Dealer()
deal.random_new_card()