import xmlrpclib

p = xmlrpclib.ServerProxy("http://localhost:8000")
print p.addCounter()
print p.startGame()
print "Your clinet ID is: ", p.getCounter()
print p.printBoard()

while p.getGameStatus() == str(0):
    try:
        userInput = str(raw_input("Please write a number between 0-8"))
        if p.checkValidMove(userInput):
            p.movePlayer(userInput)
            print "Your Move______________"
            print p.printBoard()
            if p.checkWinner():
                uinput = str(raw_input(p.strGameStatus()))
                p.endOrRestartGame(uinput)
            else:
                p.checkMove()
                print "Computer's Move______________"
                print p.printBoard()
                if p.checkWinner():
                    uinput = str(raw_input(p.strGameStatus()))
                    p.endOrRestartGame(uinput)
                else:
                    continue
        else:
            print "Please try again invalid move"
    except:
        print "Invalid move"

