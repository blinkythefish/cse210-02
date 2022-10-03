'''
Author: Jamin Pottle
Date: Oct 3, 2022
File: check_input.py
'''


class CheckInput():
    
    def __init__(self) -> None:
            # these are the input values that are expected from the user
        self.valid_hilo = ['h', 'l']
        self.valid_continue = ['y', 'n']

    def check_hilo(self, user_input):
        '''
            checks the user's input against the expected answers
            params: user_input - is the input from the user to be checked 
                                against valid inputs
            return: True - if the user gave a valid input
                    False - if the user did not give valid input
        '''

        check_hilo_input = user_input.strip().lower()

        if check_hilo_input in self.valid_hilo:
            return [True, check_hilo_input]

        else:
            return False

    
    def check_continue(self, user_input):
        '''
            checks the user's input against the expected answers
            params: user_input - is the input from the user to be checked 
                                against valid inputs
            return: True - if the user gave a valid input
                    False - if the user did not give valid input
        '''

        check_continue_input = user_input.strip().lower()
        
        if check_continue_input.strip().lower() in self.valid_continue:
            return [True, check_continue_input]

        else:
            return False