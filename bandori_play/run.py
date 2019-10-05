# import bandori_play
# bandori_play.start()

from client import Client
from server import Server

client = Client()
sevrer = Server()

print("Sending ... ")
client.senddata("Hello!")
