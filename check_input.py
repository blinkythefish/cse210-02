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
        self.user_guess = ''

    def check_hilo_input(self, user_input):
        '''
            checks the user's input against the expected answers
            params: user_input - is the input from the user to be checked 
                                against valid inputs
            return: True - if the user guess higher
                    False - if the user guesses lower
        '''

        check_hilo_input = user_input.strip().lower()

        if check_hilo_input in self.valid_hilo:
            self.user_guess = check_hilo_input
            return True

        else:
            return False


    def check_hilo(self, prev_number, next_number):
        '''
            checks if the user guessed correctly
            params: next_number - the number that the user is guessing against
            return: True - if the number is higher and user guessed correctly
                    False - if the number is lower and user guessed correctly
                    -1 - if user was wrong
        '''

        if next_number > prev_number and self.user_guess == 'h':
            return True
        
        elif next_number < prev_number and self.user_guess == 'l':
            return False
        
        else: 
            return -1
        
    
    def check_continue_input(self, user_input):
        '''
            checks the user's input against the expected answers
            params: user_input - is the input from the user to be checked 
                                against valid inputs
            return: True - if the user gave a valid input, returns the user input as well
                    False - if the user did not give valid input
        '''

        check_continue_input = user_input.strip().lower()
        
        if check_continue_input.strip().lower() in self.valid_continue:
            return [True, check_continue_input]

        else:
            return False