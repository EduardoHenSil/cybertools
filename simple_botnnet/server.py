import socketserver


def load_commands():
    return 'whoami', 'ls'


class BotHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).decode().strip()
        print(f'Bot with IP {self.client_address[0]} send:')
        print(data)
        for command in load_commands():
            print(f'Sending {command}')
            self.request.sendall(command.encode())
            data = self.request.recv(1024).decode().strip()
            print(data)


if __name__ == '__main__':
    HOST, PORT = '', 8000
    tcp_server = socketserver.TCPServer((HOST, PORT), BotHandler)
    try:
        tcp_server.serve_forever()
    except Exception as e:
        print(f'There was an error: {e}')
