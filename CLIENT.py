import socket

HEADER = 64
PORT = 5055
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "192.168.43.61"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))

send('HELLO WORLD')
input()
send('HEY!')
input()
send('HELLO TO ALL')
input()

send(DISCONNECT_MESSAGE)