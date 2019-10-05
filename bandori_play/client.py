from io import BytesIO
from pickle import dump, load
import socket


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('127.0.0.1', 8106))

    def loaddata(self, data):
        f = BytesIO()
        f.write(data)
        data = load(f)
        return data

    def dumpdata(self, data):
        f = BytesIO()
        dump(data, f)
        return f.getvalue()

    def senddata(self, data):
        data = self.dumpdata(data=data)
        self.sock.sendall(input().encode())
        res = self.sock.recv(1024)
        print(repr(res))
