import os
import itertools
import socket
import sys


def receive_cmd():
    HOST = sys.argv[1]
    PORT = sys.argv[2]
    return HOST, PORT


def create_socket(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        check_pwd(s)


def check_pwd(s):
    path = "C:\\Users\\gaeta\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\"
    with open(path + "passwords.txt", "r", encoding="UTF-8") as f:
        passwords = f.readlines()
        for password in passwords:
            password = password.strip()
            for variation in map(lambda x: ''.join(x),
                                 itertools.product(*([letter.lower(), letter.upper()] for letter in password))):
                enc_variation = variation.encode()
                s.send(enc_variation)
                response = s.recv(1024)
                response = response.decode("UTF-8")
                if response == "Connection success!":
                    print(variation)
                    break
            if response == "Connection success!":
                break



HOST, PORT = receive_cmd()
create_socket(HOST, int(PORT))
