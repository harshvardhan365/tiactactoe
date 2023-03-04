import random
#Create the global variable name as board for printing the board
board = ["-" , "-" , "-",
         "-" , "-" , "-",
         "-" , "-" , "-"]
#Global Varable .Help to Access anywhere from program
currentPlayer="X"
winner = None
gameRunning=True

#Define the Function name as player board for print the board from 0-9
def playerboard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-----")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-----")
    print(board[6]+"|"+board[7]+"|"+board[8])

#Create the function name as playerinput for taking input from players
def playerInput(board):
    inp =int(input("enter the a number 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "-":
        board[inp-1] =currentPlayer
    else:
        print("Already the player is there")

#Checking the winner logic for horizontal
def  checkHorizontal(board):
    global winner 
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
#Check win logic for row
 
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
#Check Diagonal win logic
def checkDiagnol(board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != "-":
            winner = board[1]
            return True
        elif board[2] == board[4] == board[6] and board[2] != "-":
            winner = board[2]
            return True
#Check For tie
def checktie(board):
     global gameRunning
     if"-" not in board:
        playerboard(board)
        print("its a tie")
        gameRunning = False
#Check For win
def checkwin():
    if checkDiagnol(board) or checkHorizontal(board) or checkRow(board):
        print(f"the winner is {winner}")
#Help to switch the player from X to O
def switchplayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
#randomize the computer input 
def computer(board):
    while currentPlayer =="O":
        position = random.randint(0,8)
        if board[position] =="-":
            board[position] = "O"
            switchplayer()

#while loop condition to keep running the program
while gameRunning:
        playerboard(board)
        playerInput(board)
        checkwin()
        checktie(board)
        switchplayer()
        computer(board)
        checkwin()
        checktie(board)