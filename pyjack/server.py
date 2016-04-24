import socket
from enum import Enum

class ServerEvent(Enum):
	SETUP = 0
	PLAY = 0
	END = 0

#Server Configs
SERVER_PUBLIC = socket.gethostname()
SERVER_HOST = ''
SERVER_PORT = 2121

#Setup Socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((SERVER_HOST, SERVER_PORT))
serversocket.listen(5)

#Main Game Loop
while True:
	(clientsocket, address) = serversocket.accept()

	#Do stuff
	#ct = client_thread(clientsocket)
	#ct.run()

serversocket.close()