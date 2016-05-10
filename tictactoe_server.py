from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import sys
import socket
from SocketServer import ThreadingMixIn
from Game import Game

class ThreadedXMLRPCServer(ThreadingMixIn,SimpleXMLRPCServer):
    pass
server = SimpleXMLRPCServer(("localhost",8000),allow_none=True)

counter = 0
class Parser():
    def __init__(self):
        global counter
        self.sessionID = counter
        self.name = Game(self.sessionID)

    def startGame(self):
        return self.name.print_start_board()

    def printBoard(self):
        return self.name.print_array_to_board()

    def getGameStatus(self):
        return str(self.name.gameStatus)

    def checkMove(self):
        self.name.check_move()

    def checkWinner(self):
        self.name.checkWinner()

    def getCounter(self):
        return str(self.sessionID)

    def addCounter(self):
        self.sessionID += 1
        return str(self.sessionID)

    def checkValidMove(self,playerCell):
        return self.name.validityCheck(playerCell)

    def movePlayer(self,playerCell):
        self.name.move_player(playerCell)

    def checkWinner(self):
        return self.name.checkWinner()

    def checkMove(self):
        self.name.check_moves()

    def strGameStatus(self):
        return self.name.strGameStatus()

    def endOrRestartGame(self,uinput):
        return self.name.endOrRestartGame(uinput)




print "listening on port 8000 session id", counter
server.register_introspection_functions()
server.register_instance(Parser())
server.serve_forever()
while True:
    server.handle_request()
