import socket
import sys
from string import ascii_lowercase, digits
from itertools import product


def receive_cmd():
    HOST = sys.argv[1]
    PORT = sys.argv[2]
    return HOST, PORT


def create_socket(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        create_pwd(s)


def create_pwd(s):
    length = 1
    is_on = True
    while is_on:
        pass_iter = product(letters_digits, repeat=length)
        for pwd in pass_iter:
            data = "".join(pwd)
            msg = data.encode()
            s.send(msg)
            response = s.recv(1024)
            response = response.decode()
            if response == "Connection success!":
                print(data)
                is_on = False
                break
        length += 1


HOST, PORT = receive_cmd()
letters_digits = ascii_lowercase + digits
create_socket(HOST, int(PORT))
