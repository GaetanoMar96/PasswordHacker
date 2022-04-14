import socket
import sys


def receive_cmd():
    HOST = sys.argv[1]
    PORT = sys.argv[2]
    message = sys.argv[3]
    return HOST, PORT, message


def create_socket(HOST, PORT, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = message.encode()
        s.send(message)
        response = s.recv(1024)
        response = response.decode()
        print(response)


def create_pwd():
    pass

HOST, PORT, message = receive_cmd()
create_socket(HOST, int(PORT), message)
