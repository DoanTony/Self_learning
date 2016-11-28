

def Player_Hand(Players):
    while True:
        player_input = int(input(Players +  " hand : "))
        if(player_input > 0 ) and (player_input <= 3):
            break
        else:
            print("Please enter a valid choice")
    return player_input

#Main program
def main():
    print("*************** Select your hand *********** \n 1.Scissor \n 2.Rock \n 3.Paper")
    while True:
        Player_1_Input = Player_Hand("Player 1")
        Player_2_Input = Player_Hand("Player 2")

        '''
        Winning Condition
        Strong > Weak
        1 > 3  OR 3 < 1
        2 > 1  OR 1 < 2
        3 > 2  OR 2 < 3
        '''

        winCond = {1 : 3, 2 : 1, 3 : 2} #Dictionnary for winning condition on Player 1 Choice

        winVal =  winCond.get(Player_1_Input) # Get the winning value against Player 2 Input

        if Player_2_Input == winVal:
            print("\nPlayer 1 Win!\n")
            break
        elif Player_2_Input == Player_1_Input:
            print("\nDraw, Restart!\n")
        else:
            print("\nPlayer 2 Win!\n")
            break


#Main module program
if __name__ == "__main__":
    main()


