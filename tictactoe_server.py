from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import sys
import socket
from SocketServer import ThreadingMixIn
import Game

server = SimpleXMLRPCServer(("localhost",8000),allow_none=True)
counter = 0
def addCounter():
    global counter
    counter+=1
    return counter

class Parser():
    def __init__(self):
        self.clientDict = {}

    def startGame(self,sessionID):
        return self.clientDict[str(sessionID)].print_start_board()

    def printBoard(self,sessionID):
        return self.clientDict[str(sessionID)].print_array_to_board()

    def getGameStatus(self,sessionID):
        return str(self.clientDict[str(sessionID)].gameStatus)

    def checkMove(self,sessionID):
        self.clientDict[str(sessionID)].check_moves()

    def setSessionID(self,sessionID):
        self.clientDict[str(sessionID)] = Game.Game(sessionID)

    def checkValidMove(self,sessionID,playerCell):
        return self.clientDict[str(sessionID)].validityCheck(playerCell)

    def movePlayer(self,sessionID,playerCell):
        self.clientDict[str(sessionID)].move_player(playerCell)

    def checkWinner(self,sessionID):
        return self.clientDict[str(sessionID)].checkWinner()

    def strGameStatus(self,sessionID):
        return self.clientDict[str(sessionID)].strGameStatus()

    def endOrRestartGame(self,sessionID,uinput):
        return self.clientDict[str(sessionID)].endOrRestartGame(uinput)
    #def removeSession(self):



print "listening on port 8000 session id", counter
server.register_introspection_functions()
server.register_function(addCounter,"generateClientID")
server.register_instance(Parser())
server.serve_forever()
while True:
    server.handle_request()

