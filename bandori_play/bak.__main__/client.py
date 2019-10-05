#!/usr/bin/env python3
# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 8106))
s.sendall(input().encode())
data = s.recv(1024)
print(repr(data))
