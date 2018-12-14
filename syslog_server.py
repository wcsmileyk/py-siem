import socket

from process_events import write_event

HOST = '127.0.0.1'
PORT = 514

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

while True:
    data, addr = server.recvfrom(1024)
    write_event(data)
