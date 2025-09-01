
## Test 8
    ## Rock Papper & Scissors 

'''                        
                ## Infinite Loop  ---------------------------------

                                        while True: 
                                            usr_command = input("Enter your command: ")
                                            if usr_command == "quit":
                                            break
                                            else: 
                                            print("You typed " + usr_command)
'''
while True:
    Playloop =  input('Hello! This is RPS Game! \nThanks for being here! \
                     \nIf you want to leave please type "exit" Is that Okay? \n'       )
    if Playloop.capitalize() == 'Exit':
        break
    else:
        print()
        ## UI /////////////////////////////////////
            ## PLAYERS-------------------------------------------------------------------------------------
                ## Player 1
        PLAYER1NAME = input('Player 1, please provide your name for game: ')
        print('Type (1) for ------- Scissors ')
        print('Type (2) for ------- Rock ')
        print('Type (3) for ------- Papper ')
        x = int(input('Type () your selection ------>> '))
        if x == 1:
            xstring = 'Scissors'
        elif x == 2:
            xstring = 'Rock'
        elif x == 3:
            xstring = 'Papper'

        print()
                ## Player 2
        PLAYER2NAME = input('Player 2, please provide your name for game:')
        print('Type (1) for ------- Scissors ')
        print('Type (2) for ------- Rock ')
        print('Type (3) for ------- Papper ')
        y = int(input('Type () your selection ------>> '))
        if y == 1:
            ystring = 'Scissors'
        elif y == 2:
            ystring = 'Rock'
        elif y == 3:
            ystring = 'Papper'
        print()



        print(f'{PLAYER1NAME}_{x}_  --- Selected: --- {xstring}')
        print(f'{PLAYER2NAME}_{y}_  --- Selected: --- {ystring}')
        print()

        ## RPS Evaluation // Game
        match x:
            case 1:
                if y == 1:
                    print(f'Its a tie!')
                elif y == 2:
                    print(f'{PLAYER2NAME} Wins! Rock over Scissors!')
                elif y == 3:
                    print(f'{PLAYER1NAME} Wins! Scissor over Papper!')
            case 2:
                if y == 1:
                    print(f'{PLAYER1NAME} Wins! Rock over Scissors!')
                elif y == 2:
                    print(f'Its a Tie, Both Rocking arround!')
                elif y == 3:
                    print(f'{PLAYER2NAME} Wins, Papper over Rock!')
            case 3:
                if y == 1:
                    print(f'{PLAYER2NAME} Wins! Scissor over Papper!')
                elif y == 2:
                    print(f'{PLAYER1NAME} Wins! Paper over Rock!')
                elif y == 3:
                    print(f'Tied! Both Pappers cant win!')
print()
print()

