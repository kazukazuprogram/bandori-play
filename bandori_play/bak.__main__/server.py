#!/usr/bin/env python3
# coding: utf-8

import socket
from threading import Thread

application_configure = {
    "port": "8106"
}


class Server:
    def __init__(self, port=int(application_configure["port"])):
        self.recv = None
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('127.0.0.1', int(application_configure["port"])))
        self.sock.listen(1)
        self.connection, self.addr = self.sock.accept()
        self.recvThread = Thread(target=self.recvLoop)
        self.recvThread.start()

    def recvLoop(self):
        while True:
            data = self.connection.recv(1024)
            if not data:
                break
            # print('data : {}, addr: {}'.format(data, self.addr))
            self.data = data.split()
            if self.recv is None or type(self.recv) != type(self.recvLoop):
                raise
            res = self.recv(data)
            if res is None:
                res = b"noResp"
            elif type(res) != bytes:
                res = str(res).encode()
            self.connection.sendall(res)


if __name__ == '__main__':
    s = Server()
