import socket
import json

ADMIN = 111111

def sendData(data):
    HOST = "localhost"
    PORT = 65432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(json.dumps(data))
    msg = s.recv(1024)
    s.close()
    return msg

def verifyAdmin(update):
    id = update.effective_message.from_user.id
    return id == ADMIN


