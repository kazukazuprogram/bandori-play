#!/usr/bin/env python3
# coding: utf-8

from io import BytesIO
from pickle import dump, load
import socket
from threading import Thread


class Server:
    def __init__(self, port=8106):
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.1', self.port))
        self.sock.listen(1)
        self.recvThread = Thread(target=self.recvLoop)
        self.recvThread.start()

    def recvLoop(self):
        self.connection, self.addr = self.sock.accept()
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            # print('data : {}, addr: {}'.format(data, self.addr))
            self.data = data.split()
            res = self.recv(data)
            if res is None:
                res = b"noResp"
            elif type(res) != bytes:
                res = str(res).encode()
            self.connection.sendall(res)

    def recv(self, data):
        print(data)

    def loaddata(self, data):
        f = BytesIO()
        f.write(data)
        data = load(f)
        return data

    def dumpdata(self, data):
        f = BytesIO()
        dump(data, f)
        return f.getvalue()

if __name__ == '__main__':
    s = Server()
