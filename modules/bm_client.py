import socket
import json

def sendData(data):
    HOST = "localhost"
    PORT = 65432

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(json.dumps(data))
    msg = s.recv(1024)
    s.close()
    return msg
