import socket
import sys

# creating the socket (establish a connection between two computers)


def create_socket():
    try:
        global host
        global port
        global s           # Here s is for socket
        host = ''          # here we will write the ip address of host
        port = 9999        # A very uncommon port so we can use this
        s = socket.socket  # creating a socket
    except socket.error as msg:
        print("Socket creation error " + str(msg))

# binding the socket with host and socket , and listening the connection


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port : " + str(port))

        s.bind((host, port))  # this is a tuple
        # Server should be continopusly listning from the various computer
        s.listen(5)
        # here 5 is the max bad requests it can listen after that it will throw the error and go in exception block

    except socket.error as msg:
        print("Socket binding error " + str(msg) + "\n" + "Retrying....")
        bind_socket()  # this is recusrion

# Establish connection with the client(Socket must be listening)


def socket_accept():
    s.accept()  # This s.accept returns 2 data , 1st is the
