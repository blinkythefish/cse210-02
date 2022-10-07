import dealer
import check_input


def main():
    dealer_random = dealer.Dealer()
    check_u_input = check_input.CheckInput()

    points = 300
    number = dealer_random.random_card()
    flag = "y"

    while points > 0 and flag == "y": 
        print(" ")
        print(f"The card is {number}")
        nextNumber = dealer_random.next_card()

        hilo_input = ''
        good_input = False

        while not good_input:
            hilo_input = input('higher (h) or lower (l): ')
            good_input = check_u_input.check_hilo_input(hilo_input)
            
        check_hilo = check_u_input.check_hilo(number, nextNumber)

        if check_hilo == True:
            print(f"Next card was: {nextNumber}")
            newPoints = points + 100
            print(f"your score is: {newPoints}")
        elif check_hilo == False:
            print(f"Next card was: {nextNumber}")
            newPoints = points + 100
            print(f"your score is: {newPoints}")
        elif check_hilo == -1:
            print(f"Next card was: {nextNumber}")
            newPoints = points - 75
            print(f"your score is: {newPoints}")
        
        else: 
            print('something is wrong')


        number = nextNumber
        points = newPoints
        flag = input(f"Play again ? y/n : ")

        
        while flag != "y" and flag != "n":
            flag = input(f'please use "y" to continue or "n" to exit: ' )
    print(f" ")
    if points == 0:
        print(f"Sorry you have {points} points , you lost the game")
    else:
        print(f"Excellente you have : {points}")

    
if __name__ == '__main__':
    main()