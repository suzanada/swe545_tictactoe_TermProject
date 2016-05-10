from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import threading
import sys
import socket
from SocketServer import ThreadingMixIn
import Game

class ThreadedXMLRPCServer(ThreadingMixIn,SimpleXMLRPCServer):
    pass
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = ThreadedXMLRPCServer(("localhost",8000),allow_none=True)
counter = 0
def addCounter():
    global counter
    counter+=1
    return counter


class Parser():
    def __init__(self):
        self.sessionID = counter
        self.clientDict = {}

    def startGame(self):
        return self.clientDict[str(self.sessionID)].print_start_board()

    def printBoard(self,sessionID):
        return self.clientDict[str(sessionID)].print_array_to_board()

    def getGameStatus(self,sessionID):
        return str(self.clientDict[str(sessionID)].gameStatus)

    def checkMove(self,sessionID):
        self.clientDict[str(sessionID)].check_move()

    def checkWinner(self,sessionID):
        self.clientDict[str(sessionID)].checkWinner()

    def getCounter(self):
        return str(self.sessionID)

    def setSessionID(self):
        self.sessionID = counter
        self.clientDict[str(self.sessionID)] = Game.Game(self.sessionID)

    def checkValidMove(self,sessionID,playerCell):
        return self.clientDict[str(sessionID)].validityCheck(playerCell)

    def movePlayer(self,sessionID,playerCell):
        self.clientDict[str(sessionID)].move_player(playerCell)

    def checkWinner(self,sessionID):
        return self.clientDict[str(sessionID)].checkWinner()

    def checkMove(self,sessionID):
        self.clientDict[str(sessionID)].check_moves()

    def strGameStatus(self,sessionID):
        return self.clientDict[str(sessionID)].strGameStatus()

    def endOrRestartGame(self,sessionID,uinput):
        return self.clientDict[str(sessionID)].endOrRestartGame(uinput)






print "listening on port 8000 session id", counter
server.register_introspection_functions()
server.register_function(addCounter,"generateClientID")
server.register_instance(Parser())
server.serve_forever()
while True:
    server.handle_request()
