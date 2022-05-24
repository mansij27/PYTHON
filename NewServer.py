import socket
import threading

PORT = 9998
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(c, addr):
    pass

def start():
    server.listen()
    print('Waiting for connections')
    while True:
        c, addr = s.accept()
        thread = threading.Thread(target=handle_client(c, addr)
        thread.start()
        print(f'[ACTIVE CONNECTIONS]{threading.active_count() - 1}')

print('[STARTING] Server is starting...')
start()

