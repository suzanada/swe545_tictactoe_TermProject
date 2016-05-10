import xmlrpclib

p = xmlrpclib.ServerProxy("http://localhost:8000")
p.setSessionID()
print str(p.generateClientID())
print p.getCounter()
sessionID = p.getCounter()

print p.startGame()
print "Your client ID is: ", p.getCounter()

print p.printBoard(sessionID)
while p.getGameStatus(sessionID) == str(0):
    try:
        userInput = str(raw_input("Please write a number between 0-8"))
        if p.checkValidMove(sessionID,userInput):
            p.movePlayer(sessionID,userInput)
            print "Your Move______________"
            print p.printBoard(sessionID)
            if p.checkWinner(sessionID):
                uinput = str(raw_input(p.strGameStatus(sessionID)))
                p.endOrRestartGame(sessionID,uinput)
                print p.printBoard(sessionID)
            else:
                p.checkMove(sessionID)
                print "Computer's Move______________"
                print p.printBoard(sessionID)
                if p.checkWinner(sessionID):
                    uinput = str(raw_input(p.strGameStatus(sessionID)))
                    p.endOrRestartGame(sessionID,uinput)
                    print p.printBoard(sessionID)
                else:
                    continue
        else:
            print "Please try again invalid move"
    except:
        print "Invalid move"

