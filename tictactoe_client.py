import xmlrpclib
import sys
import select

p = xmlrpclib.ServerProxy("http://localhost:8000")

sessionID = p.generateClientID()
p.setSessionID(sessionID)
print p.startGame(sessionID)
print "Your client ID is: ",sessionID


print p.printBoard(sessionID)
while p.getGameStatus(sessionID) == str(0):
    try:
        print "Please write a number between 0 and 8 (0 and 8 included).You only have 15 seconds or you will lose !"
        fi, se, th = select.select([sys.stdin], [], [], 15 )
        if (fi):
            userInput =str(sys.stdin.readline().strip())
            if p.checkValidMove(sessionID,userInput):
                p.movePlayer(sessionID,userInput)
                print "Your Move______________"
                print p.printBoard(sessionID)
                if p.checkWinner(sessionID):
                    print p.strGameStatus(sessionID)
                    fi, se, th = select.select([sys.stdin], [], [], 15 )
                    if (fi):
                        uinput =str(sys.stdin.readline().strip())
                        p.endOrRestartGame(sessionID,uinput)
                        print p.printBoard(sessionID)
                    else:
                        p.removeSession(sessionID)
                        print "Your answer was late. If you want to play, please start again."
                        break

                else:
                    p.checkMove(sessionID)
                    print "Computer's Move______________"
                    print p.printBoard(sessionID)
                    if p.checkWinner(sessionID):
                        print p.strGameStatus(sessionID)
                        fi, se, th = select.select([sys.stdin], [], [], 15 )
                        if (fi):
                            uinput =str(sys.stdin.readline().strip())
                            p.endOrRestartGame(sessionID,uinput)
                            print p.printBoard(sessionID)
                        else:
                            p.removeSession(sessionID)
                            print "Your answer was late. If you want to play, please start again."
                            break
                    else:
                        continue
            else:
                print "Please try again invalid move"
        else:
            p.removeSession(sessionID)
            print "YOU LOST! Your answer was late. If you want to play, please start again."
            break
    except:
        print "Invalid move, this is not even an integer"



