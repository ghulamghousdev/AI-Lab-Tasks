def game():
    print("Enter Player1 Name: ")
    playerOne = input()
    print("Enter Player2 Name: ")
    playerTwo = input()
    playList = ["rock", "paper", "scissors"]
    playingFlag = True
    while(playingFlag):
        print("\n\nSelect one of the play from following list: ")
        print (playList)
        print("\nEnter play for",playerOne,":")
        playerOnePlay = str(input())
        print("Enter play for",playerTwo,":")
        playerTwoPlay = str(input())
        if ((playerOnePlay=="rock" or playerOnePlay=="paper" or playerOnePlay=="scissors") and (playerTwoPlay=="rock" or playerTwoPlay=="paper" or playerTwoPlay=="scissors")):
            if playerOnePlay==playerTwoPlay:
                print("Nobody wins. Best of Luck for the next time :)")
            
            elif playerOnePlay=="rock" and playerTwoPlay=="paper":
                print (playerTwo,"wins! Congratulation!")

            elif playerOnePlay=="paper" and playerTwoPlay=="rock":
                print (playerOne,"wins! Congratulation!")

            elif playerOnePlay=="rock" and playerTwoPlay=="scissors":
                print (playerOne,"wins! Congratulation!")

            elif playerOnePlay=="scissors" and playerTwoPlay=="rock":
                print (playerTwo,"wins! Congratulation!")
    
            elif playerOnePlay=="paper" and playerTwoPlay=="scissors":
                print (playerTwo,"wins! Congratulation!")

            elif playerOnePlay=="scissors" and playerTwoPlay=="paper":
                print (playerOne,"wins! Congratulation!")
                
            entery = int(input("Enter 1 to play again or any other number to exit: "))
            if(entery!= 1):
                playingFlag = False
        else:
            entery = int(input("Invalid Play. Enter 1 to play again or any other number to exit: "))
            if(entery!=1):
                playingFlag = False
        
game()
