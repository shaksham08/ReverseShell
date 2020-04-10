import socket
import os  # Operating system
import subprocess  # processes on our computer

s = socket.socket()
host = "192.168.43.42"
port = 9999

s.connect((host, port))
