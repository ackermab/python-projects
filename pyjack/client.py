import socket
from enum import Enum

class ClientEvent(Enum):
	SETUP = 0
	WAIT = 1
	PLAY = 2
	END = 3

#Server Configs
SERVER_PUBLIC = socket.gethostname()
SERVER_HOST = ''
SERVER_PORT = 2121
CLIENT_EVENT = ClientEvent.SETUP

class PyJackServerSocket:
	""" Socket for the Black Jack Server
	"""

	def __init__(self, serversocket=None):
		if serversocket is None:
			self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		else:
			self.serversocket = serversocket

	def connect(self, host, port):
		self.serversocket.connect((host, port))

	def close(self):
		self.serversocket.close()

	def send(self, msg):
		
		totalsent = 0
		while totalsent < MSGLEN:
			sent = self.serversocket.send(msg[totalsent:])
			
			if sent == 0:
				raise RuntimeError("socket connection broken")
			
			totalsent = totalsent + sent

	def receive(self):
		
		chunks = []
		bytes_recd = 0
		while bytes_recd < MSGLEN:
			chunk = self.serversocket.recv(min(MSGLEN - bytes_recd, 2048))

			if chunk == b'':
				raise RuntimeError("socket connection broken")

			chunks.append(chunk)
			bytes_recd = bytes_recd + len(chunk)

		return b''.join(chunks)

s = PyJackServerSocket()
s.connect(SERVER_HOST, SERVER_PORT)

#Main Client Game Loop
while True:
	if CLIENT_EVENT is ClientEvent.SETUP:
		print("setting up")
		CLIENT_EVENT = ClientEvent.WAIT

	if CLIENT_EVENT is ClientEvent.WAIT:
		print("waiting for seat at the table")

		print("skipping to end")
		CLIENT_EVENT = ClientEvent.END

	if CLIENT_EVENT is ClientEvent.PLAY:
		print("playing game")

	if CLIENT_EVENT is ClientEvent.END:
		print("thanks for playing")
		break;

s.close()