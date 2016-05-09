import random

class Board:

    winnerList = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def __init__(self,sessionID):
        self.sessionID =sessionID
        self.gameArray = ["_","_","_","_","_","_"," "," "," "]
        self.startingNumber = int(random.choice("0268"))
        self.gameArray[self.startingNumber] ="X"
        self.gameStatus = 0
    @classmethod
    def print_start_board(self):

        return "Hello there, This is a basic TicTacToe Game\n\
You will never beat me, If you are lucky there will be a tie\n\
Board is set up as follows:                           \n\
                  _0_|_1_|_2_  \n\
                  _3_|_4_|_5_  \n\
                   6 | 7 | 8   \n\
"

    def print_array_to_board(self):
        gArray = self.gameArray
        return gArray[0] + "|"+ gArray[1]+"|"+ gArray[2] +"\n"+gArray[3]+ "|"+ gArray[4]+"|"+ gArray[5]+"\n"+gArray[6]+ "|"+ gArray[7]+"|"+ gArray[8]

    def move_Player(self,playerCell):
        self.gameArray[playerCell] = "O"

    def endOrRestartGame(self):
        uinput = raw_input(self.strGameStatus())
        if uinput == "y":
            self.gameStatus=0
            self.startingNumber = int(random.choice("0268"))
            self.gameArray= self.gameArray = ["_","_","_","_","_","_"," "," "," "]
            self.gameArray[self.startingNumber] ="X"
            self.print_start_board()



    def emptyCellCheck(self):
        emptyStr = ""
        for index, val in enumerate(self.gameArray):
            if val == " " or val == "_":
                emptyStr += str(index)
        return emptyStr

    def validityCheck(self,playerCell):
        if playerCell>-1 and playerCell<9 :
            if str(self.gameArray[playerCell]) == " " or str(self.gameArray[playerCell])=="_":
                return True
            else:
                return False
        else:
            return False
    def strGameStatus(self):
        if self.gameStatus==0:
            return
        elif self.gameStatus==1:
            return "HA HA COMPUTER WON Do you want to play again? (y/n)"
        elif self.gameStatus==2:
            return "Oops, YOU WON! How did that happen? Do you want to play again? (y/n)"
        else:
            return "It's a tie! Do you want to play again? (y/n)"

    def checkWinner(self):
        gArray = self.gameArray
        for i in self.winnerList:
            oCounter = 0
            xCounter = 0
            for j in i:
                if gArray[j] == "O":
                    oCounter += 1
                elif gArray[j] == "X":
                    xCounter += 1
                else:
                    continue
            if xCounter == 3:
                self.gameStatus=1
                self.endOrRestartGame()
                return
            elif oCounter==3:
                self.gameStatus=2
                self.endOrRestartGame()
                return
            else:
                continue
        emptyStr= self.emptyCellCheck()
        if emptyStr == "":
            self.gameStatus = 3
            self.endOrRestartGame()
        else:
            self.gameStatus = 0
            self.check_move()
            print "__COMPUTER'S MOVE___________________________________________"
            print self.print_array_to_board()

    def check_move(self):
        gArray = self.gameArray
        for i in self.winnerList:
            oCounter = 0
            xCounter = 0
            emptyCell = []
            for j in i:
                if gArray[j] == "O":
                    oCounter += 1
                elif gArray[j] == "X":
                    xCounter += 1
                else:
                    emptyCell.append(j)
            if xCounter == 2 and oCounter == 0 :
                if self.validityCheck(int(emptyCell[0])):
                    self.gameArray[emptyCell[0]] = "X"
                    self.gameStatus =1
                    self.endOrRestartGame()
                    return
            elif oCounter == 2 and xCounter == 0 :
                if self.validityCheck(int(emptyCell[0])):
                    self.gameArray[emptyCell[0]] = "X"
                    return
            else:
                continue
        emptyStr = self.emptyCellCheck()
        listEmptyStr = list(emptyStr)
        if emptyStr=="":
            self.gameStatus = 3
            self.endOrRestartGame()
        elif len(listEmptyStr)==1:
            self.gameArray[int(listEmptyStr[0])]= "X"
            self.gameStatus=3
            self.endOrRestartGame()
        else:
            a = int(random.choice(self.emptyCellCheck()))
            self.gameArray[a] = "X"





c= Board(1)
print c.print_start_board()
print c.print_array_to_board()

while c.gameStatus == 0:
    try:
        userInput = int(raw_input("Please write a number between 0-8"))
        if c.validityCheck(userInput):
            c.move_Player(int(userInput))
            print "__YOUR MOVE____________________________________________"
            print c.print_array_to_board()
            c.checkWinner()
        else:
            print "Please try again invalid move"
    except:
        print "Please try again invalid move"





