import random


class Game:
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

    def move_player(self,playerCell):
        playerCell = int(playerCell)
        self.gameArray[playerCell] = "O"

    def emptyCellCheck(self):
        emptyStr = ""
        for index, val in enumerate(self.gameArray):
            if val == " " or val == "_":
                emptyStr += str(index)
        return emptyStr

    def validityCheck(self,playerCell):
        playerCell = int(playerCell)
        if playerCell>-1 and playerCell<9 :
            if str(self.gameArray[playerCell]) == " " or str(self.gameArray[playerCell])=="_":
                return True
            else:
                return False
        else:
            return False
    def check_moves(self):
        gArray = self.gameArray
        xList = []
        oList=[]
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
                    xList.append(int(emptyCell[0]))
            elif oCounter == 2 and xCounter == 0 :
                if self.validityCheck(int(emptyCell[0])):
                    oList.append(int(emptyCell[0]))
            else:
                continue
        if len(xList) != 0:
            self.gameArray[xList[0]] = "X"
            self.gameStatus = 1
        elif len(oList) != 0:
            self.gameArray[oList[0]] = "X"
        else:
            emptyStr = self.emptyCellCheck()
            listEmptyStr = list(emptyStr)
            if emptyStr=="":
                self.gameStatus = 3
            elif len(listEmptyStr)==1:
                self.gameArray[int(listEmptyStr[0])]= "X"
                self.gameStatus=3
            else:
                a = int(random.choice(self.emptyCellCheck()))
                self.gameArray[a] = "X"

    def strGameStatus(self):
        if self.gameStatus==0:
            return
        elif self.gameStatus==1:
            return  "HA HA COMPUTER WON Do you want to play again? (y/n)"
        elif self.gameStatus==2:
            return "Oops, YOU WON! How did that happen? Do you want to play again? (y/n)"
        else:
            return "It's a tie! Do you want to play again? (y/n)"

    def checkWinner(self):
        if self.gameStatus == 0:
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
                    return True
                elif oCounter==3:
                    self.gameStatus=2
                    return True
                else:
                    continue
            emptyStr= self.emptyCellCheck()
            if emptyStr == "":
                self.gameStatus = 3
                return True
            else:
                return False
        else:
            return True

    def endOrRestartGame(self,uinput):
        if uinput == "y":
            self.gameStatus=0
            self.startingNumber = int(random.choice("0268"))
            self.gameArray= self.gameArray = ["_","_","_","_","_","_"," "," "," "]
            self.gameArray[self.startingNumber] ="X"
            return self.print_start_board()
        else:
            return

